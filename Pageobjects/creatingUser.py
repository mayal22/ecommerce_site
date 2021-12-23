import time
from Pageobjects.login import Logins
from Utilities.ReadDrivers import User_Management
from Utilities.ReadData import Links
from selenium.webdriver.common.by import By
class CreatingUser(Logins):
    def open_user_Management(self):
        dataset = self.driver.find_element(By.CSS_SELECTOR,User_Management.cap_menu())
        links= dataset.find_elements(By.TAG_NAME,User_Management.cap_links())
        for each in links:
            if each.get_attribute("href") == Links.userManagementLink():
                Logins.open_tab(Links.userManagementLink())
                break
    def create_users(self,first,last,email,password,confirm):
        self.driver.find_element(By.CSS_SELECTOR,User_Management.cap_create_button()).click()
        Logins.explicit_wait_on_title("User Management | Create User")
        self.driver.find_element(By.ID,User_Management.cap_first_name()).send_keys(first)
        self.driver.find_element(By.ID,User_Management.cap_last_name()).send_keys(last)
        self.driver.find_element(By.ID,User_Management.cap_email_data()).send_keys(email)
        self.driver.find_element(By.ID,User_Management.cap_password_data()).send_keys(password)
        self.driver.find_element(By.ID,User_Management.cap_confirmPassword_data()).send_keys(confirm)
    def user_checkboxes(self,active=True,confirmed=True,send_email=False):
        boxes = self.driver.find_elements(By.CLASS_NAME,User_Management.cap_checkboxes())
        for each in boxes:
            inputt = each.find_element(By.TAG_NAME,"input")
            if inputt.get_attribute("name") == "status" and active == False:
                self.driver.implicitly_wait(3)
                time.sleep(5)
                inputt.click()
            if inputt.get_attribute("name") == "confirmed" and confirmed == False:
                self.driver.implicitly_wait(3)
                time.sleep(5)
                inputt.click()
            if inputt.get_attribute("name") == "confirmation_email" and send_email == True:
                breakpoint()
                inputt.click()
                time.sleep(3)
    def Associated_Roles(self,role):
        all_roles = self.driver.find_elements(By.CLASS_NAME,User_Management.cap_radiobuttons())
        available_roles = []
        for each in all_roles:
            available_roles.append(each.text)
        try:
            available_roles(role).click()
        except TypeError:
            print(f"your role value must range between 0 to {len(available_roles)} Your given value is {role}")


            

             
        
        
        