import configparser
config = configparser.ConfigParser()
config.read("D:\\Men rocks site\\configrations\\config.ini")

class LoginData:
    @staticmethod
    def get_email():
        email = config.get("login data","email")
        return email
    @staticmethod
    def get_frontedurl():
        frontend = config.get("login data","frontend")
        return frontend
    @staticmethod
    def get_backend():
        backend = config.get("login data","backend")
        return backend
    @staticmethod
    def get_password():
        password = config.get("login data","password")
        return password
