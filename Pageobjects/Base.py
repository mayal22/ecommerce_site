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
    def submitting_form(cls,locator):
        WebDriverWait(cls.drivers,10).until(EC.visibility_of_element_located(locator))
        cls.drivers.implicitly_wait(5)
        cls.drivers.find_element(By.CSS_SELECTOR,locator).click()
        
        

        

        