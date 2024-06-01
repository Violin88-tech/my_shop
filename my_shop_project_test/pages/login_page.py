import time

import allure
from selene import browser, have, be, by
import config


class LoginPage:
    with allure.step("Open the authorization form"):
        def open_form(self):
            browser.element('.tabs-button[href="#"]').click()
            return self
    #
    # with allure.step("Assert name the authorization form"):
    #     def assert_name_form(self):
    #         browser.element('.popup-modal__window__header').should(have.text('Вход и регистрация'))
    #         return self
    #
    # with allure.step("Open the authorization form with email"):
    #     def log_in_with_password(self):
    #         browser.element('.popup-modal__window').element(by.text('Войти по паролю')).click()
    #         time.sleep(2)
    #         return self
    #
    # with allure.step("Filling the authorization form email"):
    #     def fill_user_email(self):
    #         browser.element('#email').should(be.blank).type(config.settings.USER_EMAIL)
    #         return self
    #
    # with allure.step("Filling the authorization form positive"):
    #     def fill_password_positive(self):
    #         browser.element('#pass').type(config.settings.PASSWORD)
    #         return self
    #
    # with allure.step("Filling the authorization form password"):
    #     def fill_password_negative(self):
    #         browser.element('#pass').type('123')
    #         return self
    #
    # with allure.step("Submit the form"):
    #     def submit_the_form(self):
    #         browser.element('.popup-modal__window').element(by.text('Войти')).click()
    #         return self
    #
    # def repeat_submit_the_form(self):
    #     self.open_form()
    #     self.log_in_with_password()
    #     self.fill_user_email()
    #     self.fill_password_positive()
    #     self.submit_the_form()
    #     return self
    #
    # with allure.step("Checking that user has been authorized"):
    #     def assert_authorization(self):
    #         browser.element('[href="#"] .no-tablet').should(have.text('Мой кабинет'))
            return self


login = LoginPage()
