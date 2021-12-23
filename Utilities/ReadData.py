import configparser
config = configparser.ConfigParser()
config.read("D:\\Men rocks site\\configrations\\config.ini")

class LoginData:
    @staticmethod
    def get_email():
        email = config.get("login data","email")
        return email
    @staticmethod
    def get_password():
        password = config.get("login data","password")
        return password
class Links:
    @staticmethod
    def userManagementLink():
        links = config.get("site urls","user Management link")
        return links
    @staticmethod
    def get_backend():
        backend = config.get("site urls","backend")
        return backend
    @staticmethod
    def get_frontedurl():
        frontend = config.get("site urls","frontend")
        return frontend

