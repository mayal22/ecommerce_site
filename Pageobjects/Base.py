import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.ReadDrivers import User_Management
class basic:
    @classmethod
    def createdriver(cls,driver):
        if driver == "chrome":
            cls.drivers = webdriver.Chrome(executable_path="D:\\Tasks ERP\\PageObjects\\chromedriver.exe")
        return cls.drivers
    @classmethod
    def open_tab(cls,url):
        cls.drivers.execute_script("window.open('');")
        cls.drivers.switch_to.window(cls.drivers.window_handles[1])
        cls.drivers.get(url)
    @classmethod
    def explicit_wait_on_title(cls,title):
        WebDriverWait(cls.drivers,10).until(EC.title_is(title))
        return cls.drivers.title
    @classmethod
    def submitting_form(cls,elementt,message,locator=1):
        # try:
            if locator == 1:
                values = cls.drivers.find_element(By.CSS_SELECTOR,elementt)
                WebDriverWait(cls.drivers,15).until(EC.visibility_of(values))
                print("entering the scroll down")
                cls.drivers.execute_script("window.scrollTo(0,6000)")
                time.sleep(10)
                values.click()
                # # try:
                # valuess = cls.drivers.find_element(By.CSS_SELECTOR,message)
                # WebDriverWait(cls.drivers,10).until(EC.visibility_of(valuess))
                # time.sleep(2)
                # # except:

            elif locator == 2:
                values= cls.drivers.find_element(By.ID,elementt)
                valuess = cls.drivers.find_element(By.CSS_SELECTOR,message)
                WebDriverWait(cls.drivers,15).until(EC.visibility_of(values))
                values.click()
                
                # WebDriverWait(cls.drivers,10).until(EC.visibility_of(valuess))
            elif locator == 3:
                values =cls.drivers.find_element(By.TAG_NAME,elementt)
                valuess = cls.drivers.find_element(By.CSS_SELECTOR,message)
                WebDriverWait(cls.drivers,15).until(EC.visibility_of(values))
                values.click()
                # WebDriverWait(cls.drivers,10).until(EC.visibility_of(valuess))
            elif locator ==4:
                values = cls.drivers.find_element(By.CLASS_NAME,elementt)
                WebDriverWait(cls.drivers,15).until(EC.visibility_of(values))
                valuess = cls.drivers.find_element(By.CSS_SELECTOR,message)
                values.click()
                # WebDriverWait(cls.drivers,10).until(EC.visibility_of(valuess))
            elif locator ==5:
                values =cls.drivers.find_element(By.XPATH,elementt)
                valuess = cls.drivers.find_element(By.CSS_SELECTOR,message)
                WebDriverWait(cls.drivers,15).until(EC.visibility_of(values))
                values.click()
                # WebDriverWait(cls.drivers,10).until(EC.visibility_of(valuess))
            try:
                cls.drivers.find_element(By.CSS_SELECTOR,User_Management.cap_successful_alert())
            except:
                cls.drivers.find_element(By.CSS_SELECTOR,User_Management.cap_error_alert())
                
        # except:
            # print(f"locator value is invalid like , locators value range between 1 to 5\n Your present value is {locator}")
            # return valuess.text
    @classmethod
    def success_alert_messages(cls):
        try:
            success_element = cls.drivers.find_element(By.CSS_SELECTOR,User_Management.cap_successful_alert())
            WebDriverWait(cls.drivers,10).until(EC.visibility_of(success_element))
            return success_element.text.split("\n")
        except:
            failed_element = cls.drivers.find_element(By.CSS_SELECTOR,User_Management.cap_error_alert())
            WebDriverWait(cls.drivers,10).until(EC.visibility_of(failed_element))
            return failed_element.text.split("\n")
            



        
        

        

        