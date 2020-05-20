import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = True
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    CONFIG_NAME = "config.DevConfig"
    HOST_MACHINE = os.getenv("DEV_HOST_MACHINE")
    HOST = os.getenv("DEV_HOST")
    WEB_HOST = os.getenv("DEV_WEB_HOST")
    DB_USERNAME = os.getenv("DEV_DB_USERNAME")
    DB_PASSWORD = os.getenv("DEV_DB_PASSWORD")
    DB_HOSTNAME = os.getenv("DEV_DB_HOSTNAME")
    DB_NAME = os.getenv("DEV_DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"


class ProdConfig(Config):
    CONFIG_NAME = "config.ProdConfig"
    HOST_MACHINE = os.getenv("PROD_HOST_MACHINE")
    HOST = os.getenv("PROD_HOST")
    WEB_HOST = os.getenv("PROD_WEB_HOST")
    DB_USERNAME = os.getenv("PROD_DB_USERNAME")
    DB_PASSWORD = os.getenv("PROD_DB_PASSWORD")
    DB_HOSTNAME = os.getenv("PROD_DB_HOSTNAME")
    DB_NAME = os.getenv("PROD_DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"
