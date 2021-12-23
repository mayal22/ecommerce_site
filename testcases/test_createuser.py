import pytest
from Pageobjects.creatingUser import CreatingUser
from Utilities.ReadDrivers import User_Management
# from Pageobjects.Base import basic
user_data = [("Arun","sharma","amsharma@gmail.com","arunnn","arunnn"),("Harsh","baweja","harshh","harshh")]
def test_Create_user_A(Loggedin):
    object = CreatingUser()
    object.open_user_Management()
    object.create_users("first","second","email1@gmail","password","password")
    print("entering")
    object.user_checkboxes(send_email=True)
    object.Associated_Roles(1)
    object.submitting_form(User_Management.cap_submitUser())

