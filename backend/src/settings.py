import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
ROOT = Path(__file__).parent.parent


class BaseConfit:
    SECRET_KEY = b"0yy0lYd6o4Yqv3v99kt1J7VtJRbq44z8CVkTBw3Aagg="
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(ROOT.joinpath("data", "data.dev.db"))
    VALIDITY_INCREMENT = 7200


class DevelopmentConfig(BaseConfit): ...


class TestingConfig(BaseConfit): ...


class ProductionConfig(BaseConfit): ...


def get_config(environment: str | None = None):
    environment = environment if environment else os.getenv("ENVIRONMENT")
    match environment:
        case "production":
            return ProductionConfig
        case "testing":
            return TestingConfig
        case "development":
            return DevelopmentConfig
        case _:
            return DevelopmentConfig
