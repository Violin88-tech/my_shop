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
        time.sleep(2)
        login.open_form()
        time.sleep(2)
        login.log_in_with_password()
        time.sleep(2)
        login.fill_user_email()
        login.fill_password_positive()
        login.submit_the_form()
        login.repeat_submit_the_form()


