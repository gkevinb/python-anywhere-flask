class Config(object):
    DEBUG = True
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    CONFIG_NAME = "config.DevConfig"
    HOST_MACHINE = "flask607"
    HOST = "http://0.0.0.0:5000/"
    DB_USERNAME = "root"
    DB_PASSWORD = "admin"
    DB_HOSTNAME = "db123"
    DB_NAME = "db"
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"


class ProdConfig(Config):
    CONFIG_NAME = "config.ProdConfig"
    HOST_MACHINE = "blue-liveweb2"
    HOST = "https://gkevinb.pythonanywhere.com/"
    DB_USERNAME = "gkevinb"
    DB_PASSWORD = "64zd32xk"
    DB_HOSTNAME = "gkevinb.mysql.pythonanywhere-services.com"
    DB_NAME = "gkevinb$flask"
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"
