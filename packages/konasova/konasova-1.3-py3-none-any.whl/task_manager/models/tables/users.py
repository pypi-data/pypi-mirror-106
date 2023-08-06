import uuid
from task_manager.models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from task_manager.models.mixins import AuthMixin, OutputMixin


class User(Base, AuthMixin, OutputMixin):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), nullable=False)
    passwordHash = Column(String(120), nullable=False)
    surname = Column(String(120))
    email = Column(String(120), nullable=False)
    about = Column(String(120))
    telegram = Column(String(120))
    phone = Column(String(120))
    skype = Column(String(120))
    slack = Column(String(120))
    userSpace = Column(UUID(as_uuid=True))
    spaces = Column(ARRAY(UUID(as_uuid=True)))

    def __init__(self, name, passwordHash, email):
        self.name = name
        self.passwordHash = passwordHash
        self.email = email

    def __str__(self):
        return "User(id='%s')" % self.id


class RevokedTokenModel(Base, AuthMixin):
    __tablename__ = 'revoked_tokens'
    id = Column(Integer, primary_key=True)
    jti = Column(String(120))
