# pylint: disable=no-name-in-module
import re, json
import orjson
from uuid import UUID
from pydantic import BaseModel, validator
from fastapi_jwt_auth import AuthJWT
from task_manager.common_api.Api import conf_common_api
from typing import Optional, List


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()

class BaseMixin(BaseModel):

    def to_json(self):
        return json.loads(self.json())

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

class AuthUser(BaseModel):
    email: str
    passwordHash: str

    @validator('email')
    def email_match(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('email not validate')
        else:
            return v


class RequestRegisterUser(AuthUser):
    name: str

class Settings(BaseModel):
    authjwt_secret_key: str = conf_common_api.get('fastapi', 'JWT_SECRET_KEY')
    authjwt_token_location: set = {conf_common_api.get('fastapi', 'JWT_STORAGE')}
    authjwt_cookie_csrf_protect: bool = True


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()



class Credentionals(BaseModel):
    accessToken: str
    refreshToken: str



class UserResponse(BaseMixin):

    id: UUID
    name: str
    surname: Optional[str]
    email: str
    about: Optional[str]
    telegram: Optional[str]
    phone: Optional[str]
    skype: Optional[str]
    slack: Optional[str]
    userSpace: Optional[UUID]
    spaces: Optional[List[UUID]]

    class Config:
        orm_mode = True


class UpdateUserRequest(BaseMixin):
    name: str
    surname: str
    email: str
    about: str
    telegram: str
    phone: str
    skype: str
    slack: str


    @validator('email')
    def email_match(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('email not validate')
        else:
            return v



class AuthResponse(BaseMixin):
    credentionals: Credentionals
    user: UserResponse

class StatusResponse(BaseModel):
    status: int


class RefreshTokenResponse(BaseModel):
    access_token: str
    refresh_token: str

class Error(BaseModel):
    text: str

class ErrorResponse(BaseModel):
    error: Error


class NewPasswordRequest(BaseModel):
    passwordHashOld: str
    passwordHashNew: str