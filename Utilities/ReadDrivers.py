import configparser
config = configparser.ConfigParser()
config.read("D:\\Men rocks site\\configrations\\drivers.ini")

class LoginDrivers:
    @staticmethod
    def cap_email():
        email = config.get("login drivers","email id")
        return email
    @staticmethod
    def cap_password():
        password = config.get("login drivers","password id")
        return password
    @staticmethod
    def cap_loginbutton():
        loginbutton = config.get("login drivers","login button css")
        return loginbutton
    @staticmethod
    def cap_forgetPassword():
        forget = config.get("login drivers","forget password css")
        return forget
    @staticmethod
    def cap_remember():
        remember = config.get("login drivers","remember checkbox id")
        return remember