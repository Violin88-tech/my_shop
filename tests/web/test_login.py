import time

import pytest
import allure
from my_shop_project_test.pages.login_page import login
from my_shop_project_test.pages.main_page import main
import config


@allure.epic('WEB.Authorized')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestAuthorization:

    @allure.title("Verifying successful user authorization")
    def test_authorization_registered_user(self):
        main.open_shop_page()
        time.sleep(1)
        login.open_form()
        time.sleep(1)
    #     login.assert_name_form()
    #     time.sleep(1)
    #     login.log_in_with_password()
    #     login.fill_user_email()
    #     login.fill_password_positive()
    #     login.submit_the_form()
    #     login.repeat_submit_the_form()
    #     login.assert_authorization()
    #
    # @allure.title("Verifying unsuccessful user authorization")
    # def test_authorization_unregistered_user(self):
    #     main.open_shop_page()
    #
    #     login.open_form()
    #     login.assert_name_form()
    #     login.log_in_with_password()
    #     login.fill_user_email()
    #     login.fill_password_negative()
    #     login.submit_the_form()
    #     login.assert_name_form()
