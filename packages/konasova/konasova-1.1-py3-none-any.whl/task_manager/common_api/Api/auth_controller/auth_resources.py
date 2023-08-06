
import uuid
from fastapi import Depends, Request
from task_manager.common_api.Api import CommonApi, db
from functools import wraps
from sqlalchemy.future import select  
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_restful import Resource, set_responses
from fastapi.exceptions import RequestValidationError, RequestErrorModel
from fastapi_jwt_auth.exceptions import AuthJWTException
from .dataclases import (
    RequestRegisterUser, AuthUser, AuthJWT, 
    StatusResponse, RefreshTokenResponse,
    AuthResponse, Credentionals, UserResponse, NewPasswordRequest, UpdateUserRequest
)
from .routines import JSONErrorResponse, error_types_responses
from task_manager.models import User
from .crud import save_to_db, add_token_to_blacklist, is_jti_blacklisted, update_password, update_user_data, check_auth_user
from .exceptions import HTTPCommonException


@CommonApi.exception_handler(AuthJWTException)
async def authjwt_exception_handler(request: Request,exc: AuthJWTException):
    return JSONErrorResponse(
        status_code=exc.status_code,
        text= exc.message
    )

@CommonApi.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    msg = exc.errors()[0]['msg']
    if msg == 'field required':
        msg = f"Требуется следующее поле: {exc.errors()[0]['loc'][1]}"
    return JSONErrorResponse(status_code=400, text=msg)


@CommonApi.exception_handler(500)
async def bad_request_exception_handler(request: Request, exc: RequestErrorModel):
    return JSONErrorResponse(status_code=500, text="Что-то пошло не так")


@CommonApi.exception_handler(HTTPCommonException)
async def common_exception_handler(request: Request, exc: HTTPCommonException):
    return JSONErrorResponse(status_code=exc.status_code, text=exc.message)


class UserRegistration(Resource):
    @set_responses(
        StatusResponse,
        200,
        error_types_responses(500,422,409,400),
        tags=["auth"]
    )
    async def post(self, user: RequestRegisterUser, authorize: AuthJWT = Depends()):
        """ Регистрация пользователя """
        new_user = User(name=user.name, passwordHash=User.generate_hash(user.passwordHash), email=user.email)
        if await save_to_db(new_user):
            return JSONResponse(status_code=200, content=StatusResponse(status=0).dict())
        else:
            return JSONErrorResponse(status_code=409, text=f"Пользователь с данным email {user.email} уже существует")

            

class UserAuth(Resource):
    @set_responses(
        AuthResponse,
        200,
        error_types_responses(500,422,401,404),
        tags=["auth"]
    )
    async def post(self, user: AuthUser, authorize: AuthJWT = Depends()):
        """ Запрос на авторизацию """
        auth_response = await check_auth_user(user, authorize)
        return JSONResponse(status_code=200,content=auth_response.to_json())

class UserLogout(Resource):
    @set_responses(
        StatusResponse,
        200,
        error_types_responses(500,422),
        operation_id="authorize_access_logout",
        tags=["auth"]
    )
    async def post(self, authorize: AuthJWT = Depends()):
        """ Выход пользователя """
        authorize.jwt_required()
        jti = authorize.get_raw_jwt()['jti']
        await add_token_to_blacklist(jti)
        return JSONResponse(status_code=200, content=StatusResponse(status=0).dict())


class RefreshAccessToken(Resource):
    @set_responses(
        RefreshTokenResponse,
        200,
        error_types_responses(401,422),
        operation_id="authorize_refresh_token",
        tags=["auth"]
    )
    async def post(self, authorize: AuthJWT = Depends()):
        """ Запрос на обновление access токена """
        authorize.jwt_refresh_token_required()
        jti = authorize.get_raw_jwt()['jti']

        if await is_jti_blacklisted(jti):
            return JSONErrorResponse(status_code=401, text='Токен устарел')

        current_user = authorize.get_jwt_subject()
        access_token = authorize.create_access_token(subject=current_user)
        refresh_token = authorize.create_refresh_token(subject=current_user)

        return JSONResponse(status_code=200, content=RefreshTokenResponse(access_token=access_token,refresh_token=refresh_token).dict())


class CheckToken(Resource):
    @set_responses(
        StatusResponse,
        200,
        error_types_responses(401,422,500),
        operation_id="authorize_access_check_token",
        tags=["auth"]
    )
    async def get(self, authorize: AuthJWT = Depends()):
        """ Проверка актуальности access токена """
        authorize.jwt_required()
        jti = authorize.get_raw_jwt()['jti']
        if await is_jti_blacklisted(jti):
            return JSONErrorResponse(status_code=401, text='Токен устарел')
        return JSONResponse(status_code=200, content=StatusResponse(status=0).dict())


def jwt_required(func):
    @wraps(func)
    async def wrapper(authorize: AuthJWT = Depends(), *args, **kw):
        authorize.jwt_required()
        jti = authorize.get_raw_jwt()['jti']

        if await is_jti_blacklisted(jti):
            return JSONErrorResponse(status_code=401, text='Токен устарел')

        return await func(*args, **kw, authorize = authorize)
    return wrapper


class UserInfo(Resource):
    @set_responses(
        UserResponse,
        200,
        error_types_responses(404,422,500),
        operation_id="authorize_access_user_info",
        tags=["auth"]
    )
    @jwt_required
    async def get(self, id: str, authorize: AuthJWT = Depends()):
        """ Информация о конкретном пользователе """
        try:
            uuId = uuid.UUID(f'{id}')
        except ValueError as e:
            return JSONErrorResponse(status_code=400, text=str(e))
        current_user_q = await db.session.execute(select(User).filter_by(id=uuId))
        current_user = current_user_q.scalars().first()
        if current_user is None:
            return JSONErrorResponse(status_code=404, text="Пользователь не найден")
        return JSONResponse(status_code=200, content=UserResponse.from_orm(current_user).to_json())


class ChangePassword(Resource):
    @set_responses(
        StatusResponse,
        200,
        error_types_responses(403,404,422,500),
        operation_id="authorize_access_change_password",
        tags=["auth"]
    )
    @jwt_required
    async def put(self, passwords: NewPasswordRequest, authorize: AuthJWT = Depends()):
        """ Изменение пароля """
        email = authorize.get_jwt_subject()
        res_data = await update_password(passwords, email)
        return JSONResponse(status_code=200, content=res_data.dict())


class UpdateUser(Resource):
    @set_responses(
        Credentionals,
        200,
        error_types_responses(403,404,422,500),
        operation_id="authorize_access_update_user",
        tags=["auth"]
    )
    @jwt_required
    async def put(self, user_data: UpdateUserRequest, authorize: AuthJWT = Depends()):
        """ Обновление данных о пользователе """
        credentionals = await update_user_data(user_data, authorize)
        return JSONResponse(status_code=200, content=credentionals.dict())