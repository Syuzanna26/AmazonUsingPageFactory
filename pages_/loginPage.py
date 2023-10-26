from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def fill_usernamname_field(self, username):
        userNameFieldElement = self._find_element(By. ID, "ap_email")
        self._fill_field(userNameFieldElement, username)

    def click_on_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFieldElement, password)

    def click_on_signin_button(self):
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signInButtonElement)