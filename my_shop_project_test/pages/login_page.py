import time
import allure
from selene import browser, have, be, by
import config

class LoginPage:
    with allure.step("Open the authorization form"):
        def open_form(self):
            browser.element('.tabs-button[href="#"]').click()
            browser.element('.popup-modal__window__header').with_(timeout=50).should(have.text(
                'Вход и регистрация'))
            return self

    with allure.step("Open the authorization form with email"):
        def log_in_with_password(self):
            browser.element('.popup-modal__window').element(by.text('Войти по паролю')).click()
            browser.element('.popup-modal__window').with_(timeout=50).should(have.text('Войти'))
            return self

    with allure.step("Filling the authorization form email"):
        def fill_user_email(self):
            browser.element('#email').should(be.blank).type(config.settings.USER_EMAIL).with_(timeout=200)
            return self

    with allure.step("Filling the authorization form positive"):
        def fill_password_positive(self):
            browser.element('#pass').type(config.settings.PASSWORD).with_(timeout=200)
            return self

    with allure.step("Filling the authorization form password"):
        def fill_password_negative(self):
            browser.element('#pass').type('123').with_(timeout=200)
            return self

    with allure.step("Submit the form"):
        def submit_the_form(self):
            browser.element('.popup-modal__window').with_(timeout=200).element(by.text('Войти')).click()
            return self

    def repeat_submit_the_form(self):
        self.open_form()
        self.log_in_with_password()
        self.fill_user_email()
        self.fill_password_positive()
        self.submit_the_form()
        return self

login = LoginPage()
