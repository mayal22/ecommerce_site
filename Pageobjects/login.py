from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pageobjects.Base import basic
from Utilities.ReadData import Links
from Utilities.ReadDrivers import LoginDrivers
from selenium.webdriver.common.by import By
from Utilities.ReadData import LoginData
class Logins(basic):
    driver = basic.createdriver("chrome")
    def urlhit(self):
        Logins.driver.get(Links.get_backend())
    def email(self):
        Logins.driver.find_element(By.ID,LoginDrivers.cap_email()).send_keys(LoginData.get_email())
    def password(self):
        Logins.driver.find_element(By.ID,LoginDrivers.cap_password()).send_keys(LoginData.get_password())
        Logins.driver.find_element(By.ID,LoginDrivers.cap_password()).send_keys(Keys.ENTER)
    def submit_button(self):
        Logins.driver.find_element(By.CSS_SELECTOR,LoginDrivers.cap_loginbutton())
    def home_pageTitle(self):
        WebDriverWait(Logins.driver,10).until(EC.title_is("Men Rocks International | Dashboard"))
        return Logins.driver.title

        
    