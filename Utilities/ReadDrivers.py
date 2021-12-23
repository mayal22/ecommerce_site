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
class User_Management():
    @staticmethod
    def cap_menu():
        menu = config.get("user management drivers","menu css")
        return menu
    @staticmethod
    def cap_links():
        links = config.get("user management drivers","links tag")
        return links
    @staticmethod
    def cap_create_button():
        creating = config.get("user management drivers","create user button css")
        return creating
    @staticmethod
    def cap_first_name():
        firstname = config.get("user management drivers","first name data id")
        return firstname
    @staticmethod
    def cap_last_name():
        lastname = config.get("user management drivers","last name data id")
        return lastname
    @staticmethod
    def cap_email_data():
        email_name = config.get("user management drivers","email data id")
        return email_name
    @staticmethod
    def cap_email_data():
        email_name = config.get("user management drivers","email data id")
        return email_name
    @staticmethod
    def cap_password_data():
        password_name = config.get("user management drivers","password data id")
        return password_name
    @staticmethod
    def cap_confirmPassword_data():
        confirm = config.get("user management drivers","confirm password data id")
        return confirm
    @staticmethod
    def cap_checkboxes():
        checkboxes = config.get("user management drivers","checkboxes class")
        return checkboxes
    @staticmethod
    def cap_radiobuttons():
        radiobuttons = config.get("user management drivers","radiobuttons class")
        return radiobuttons
    @staticmethod
    def cap_permissions():
        PermissionButtons = config.get("user management drivers","permissions checkboxes id")
        return PermissionButtons
    @staticmethod
    def cap_submitUser():
        createUserButtons = config.get("user management drivers","submit button css")
        return createUserButtons
    