from Pageobjects.login import Logins
import pytest
@pytest.fixture
def Loggedin():
    ob = Logins()
    ob.urlhit()
    ob.email()
    ob.password()
    ob.home_pageTitle()
    yield
    Logins.driver.quit()

