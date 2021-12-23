from Pageobjects.login import Logins
def test_login():
    ob = Logins()
    ob.urlhit()
    ob.email()
    ob.password()
    assert ob.home_pageTitle() == "Men Rocks International | Dashboard","Login was not succesfull"