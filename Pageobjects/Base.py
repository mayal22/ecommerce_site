from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class basic:
    @classmethod
    def createdriver(cls,driver):
        if driver == "chrome":
            cls.drivers = webdriver.Chrome(executable_path="D:\\Tasks ERP\\PageObjects\\chromedriver.exe")
        return cls.drivers
    def open_tab(self,url):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)
        
        

        

        