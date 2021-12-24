import time
import pytest
from Pageobjects.creatingUser import CreatingUser
from Pageobjects.Base import basic
from Utilities.ReadDrivers import User_Management
# from Pageobjects.Base import basic
# user_data = [("Arun","sharma","amsharma@gmail.com","arunnn","arunnn"),("Harsh","baweja","harshh","harshh")]
def test_Create_user_A(Loggedin):
    object = CreatingUser()
    object.open_user_Management()
    object.create_users("first1145","second1121","email1145@gmail","password1199","password1199")
    object.user_checkboxes(send_email=False)
    object.Associated_Roles(1)
    basic.submitting_form(User_Management.cap_submitUser(),User_Management.cap_successful_alert(),1)
    time.sleep(5)
    assert basic.success_alert_messages()[1] == "The user was successfully created.",basic.success_alert_messages()[1]

