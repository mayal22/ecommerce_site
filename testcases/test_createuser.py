import pytest
from Pageobjects.creatingUser import CreatingUser
from Pageobjects.Base import basic
from Utilities.ReadDrivers import User_Management
# from Pageobjects.Base import basic
# user_data = [("Arun","sharma","amsharma@gmail.com","arunnn","arunnn"),("Harsh","baweja","harshh","harshh")]
def test_Create_user_A(Loggedin):
    object = CreatingUser()
    object.open_user_Management()
    object.create_users("first11","second11","email111@gmail","password11","password11")
    object.user_checkboxes(send_email=False)
    object.Associated_Roles(1)
    basic.submitting_form(User_Management.cap_submitUser(),User_Management.cap_successful_alert(),1)
    assert basic.submitting_form == "The user was successfully created.","user was not succesfully created" 


