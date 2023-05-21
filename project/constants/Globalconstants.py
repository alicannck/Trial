from selenium.webdriver.common.by import By 


URL = "https://www.saucedemo.com/"

NAME_ID = (By.ID,"user-name")
PASSWORD_ID = (By.ID,"password")
BUTTON_ID = (By.ID,"login-button")

errorMessage1 = "Epic sadface: Username is required"    # name and password emty
errorMessage2 = "Epic sadface: Password is required"    # password emty
errorMessage3 = "Epic sadface: Sorry, this user has been locked out."   #user locked out
errorMessage4 = "Epic sadface: Username and password do not match any user in this service" # not match any user in this service

LIST = [("1","1"),("2","2"),("3","3")]