import time
import allure
from selene import browser, have, be, by
import config
class LoginPage:

    @allure.step("Open the authorization form")
    def open_form(self):

        browser.element('.tabs-button[href="#"]').click()
        time.sleep(2)
        # browser.element('.popup-modal__window__header').with_(timeout=200).should(have.text(
        #         'Вход и регистрация'))

        return self

    @allure.step("Open the authorization form with email")
    def log_in_with_password(self):
        #with allure.step("Open the authorization form with email"):
        browser.element('.popup-modal__window').element(by.text('Войти по паролю')).click()
        browser.element('.popup-modal__window').with_(timeout=200).should(have.text('Войти'))
        return self

    @allure.step("Filling the authorization form email")
    #with allure.step("Filling the authorization form email"):
    def fill_user_email(self):
        browser.element('#email').should(be.blank).type(config.settings.USER_EMAIL)
        return self

    @allure.step("Filling the authorization form positive")
    #with allure.step("Filling the authorization form positive"):
    def fill_password_positive(self):
        browser.element('#pass').type(config.settings.PASSWORD)
        return self

    @allure.step("Filling the authorization form password")
    #with allure.step("Filling the authorization form password"):
    def fill_password_negative(self):
        browser.element('#pass').type('123')
        return self

    @allure.step("Submit the form")
    #with allure.step("Submit the form"):
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
