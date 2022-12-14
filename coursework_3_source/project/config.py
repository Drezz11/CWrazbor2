import base64
import os
from pathlib import Path
from typing import Type

BASE_DIR = Path(__file__).resolve().parent.parent
ALGORITHM = 'HS256'
JWT_SECRET = 's$c$adv'
PWD_HASH_SALT = base64.b64decode("salt")
PWD_HASH_ITERATIONS = 100_000


class BaseConfig:
 #  SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')


    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130


    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('project2.db').as_posix()


class ProductionConfig(BaseConfig):
    DEBUG = False
    # TODO: дополнить конфиг


class ConfigFactory:
    flask_env = os.getenv('FLASK_ENV')

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        if cls.flask_env == 'development':
            return DevelopmentConfig
        # elif cls.flask_env == 'production':
        #     return ProductionConfig
        # elif cls.flask_env == 'testing':
        #     return TestingConfig
        # raise NotImplementedError


# config = ConfigFactory.get_config()
config = DevelopmentConfig()
