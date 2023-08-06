from task_manager.models import User, RevokedTokenModel
from task_manager.common_api.Api import db
from .dataclases import AuthUser, NewPasswordRequest, UpdateUserRequest, Credentionals, StatusResponse, AuthResponse, UserResponse
from sqlalchemy.future import select   
from fastapi_jwt_auth import AuthJWT
from .exceptions import HTTPCommonException

async def check_auth_user(user: AuthUser, authorize: AuthJWT):
    """ авторизация пользователя """
    current_user_q = await db.session.execute(select(User).filter_by(email=user.email))
    current_user = current_user_q.scalars().first()
    if current_user is not None:
        if User.verify_hash(user.passwordHash, current_user.passwordHash):
            access_token = authorize.create_access_token(subject=user.email)
            refresh_token = authorize.create_refresh_token(subject=user.email)
            credentionals = Credentionals(accessToken=access_token, refreshToken=refresh_token)
            return AuthResponse(credentionals=credentionals, user=UserResponse.from_orm(current_user))
        else:
            raise HTTPCommonException(401, message="Неправильный пароль")
    else:
        raise HTTPCommonException(404, message="Пользователь не найден")

async def save_to_db(new_user: User):
    """ сохраняем пользователя в базу если его еще там нет """
    q = await db.session.execute(select(User).filter(User.email==new_user.email))
    if q.scalars().first() is not None:
        return None
    else:
        db.session.add(new_user)
        await db.session.commit()
        return 'ok'


async def update_password(passwords: NewPasswordRequest, email: str):
    """ обновляем пароль пользователя """
    user_q = await db.session.execute(select(User).filter(User.email==email))
    user = user_q.scalars().first()
    if user is None:
        raise HTTPCommonException(404, message='Пользователь не найден')

    if User.verify_hash(passwords.passwordHashOld, user.passwordHash):        
        user.passwordHash = User.generate_hash(passwords.passwordHashNew)
        await db.session.merge(user)
        await db.session.commit()
        return StatusResponse(status=0)
    else:
        raise HTTPCommonException(403, message='Существующий пароль введен некорректно')


async def update_user_data(user_data: UpdateUserRequest, authorize: AuthJWT):
    """ обновляем данные о пользователе """
    email = authorize.get_jwt_subject()
    user_q = await db.session.execute(select(User).filter(User.email==email))
    user = user_q.scalars().first()
    if user is None:
        raise HTTPCommonException(404, message='Пользователь не найден')

    user.name = user_data.name
    user.surname = user_data.surname
    users_q = await db.session.execute(select(User).filter(User.email==user_data.email))
    if len(users_q.scalars().all()) <= 1:
        user.email = user_data.email
    else:
        raise HTTPCommonException(403, message='Заданный email уже существует')
    user.about = user_data.about
    user.telegram = user_data.telegram
    user.phone = user_data.phone
    user.skype = user_data.skype
    user.slack = user_data.slack

    await db.session.merge(user)
    await db.session.commit()
    
    access_token = authorize.create_access_token(subject=user.email)
    refresh_token = authorize.create_refresh_token(subject=user.email)
    return Credentionals(accessToken=access_token, refreshToken=refresh_token)



async def add_token_to_blacklist(jti: str):
    """ добавляем токен в блэклист """
    revoked_token = RevokedTokenModel(jti = jti)
    db.session.add(revoked_token)
    await db.session.commit()


async def is_jti_blacklisted(jti):
    """ проверяем есть ли токен в блэклист """
    query = await db.session.execute(select(RevokedTokenModel).filter_by(jti = jti))
    first = query.scalars().first()
    return bool(first)

