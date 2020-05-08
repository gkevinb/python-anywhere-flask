import socket

config = {
    'DEV': {
        'HOST_MACHINE': "flask607",
        'HOST': "http://0.0.0.0:5000/",
        "DB_USERNAME": "root",
        "DB_PASSWORD": "admin",
        "DB_HOSTNAME": "db123",
        "DB_NAME": "db"
    },
    'PROD': {
        'HOST_MACHINE': "blue-liveweb2",
        'HOST': "https://gkevinb.pythonanywhere.com/",
        "DB_USERNAME": "gkevinb",
        "DB_PASSWORD": "64zd32xk",
        "DB_HOSTNAME": "gkevinb.mysql.pythonanywhere-services.com",
        "DB_NAME": "gkevinb$flask"
    }
}

def get_env_config():
    for (_, value) in config.items():
        if value.get('HOST_MACHINE') == socket.gethostname():
            return value

def load(variable):
    return get_env_config().get(variable)
