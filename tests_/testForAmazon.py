import time
from selenium import webdriver
from pages_.loginPage import LoginPage


driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
loginPageObj = LoginPage(driver)
loginPageObj.fill_usernamname_field("syuzanna26.12@gmail.com")
loginPageObj.click_on_continu_button()
loginPageObj.fill_password_field("Davit2602")
time.sleep(5)
loginPageObj.click_on_signin_button()

driver.close()