from Pageobjects.login import Logins
def test_login1():
    ob = Logins()
    ob.urlhit()
    ob.email()
    ob.password()
    ob.home_pageTitle()
    assert ob.home_pageTitle == "Men Rocks International | Dashboard","not login Successfully"