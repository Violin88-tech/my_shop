import pytest
import allure
from my_shop_project_test.pages.main_page import main


@allure.epic('WEB.Menu')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking menu items")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestMenu:

    @allure.title("Check header, body and footer menu")
    def test_main_menu(self):
        main.open_shop_page()

        main.assert_header_main_menu()
        main.assert_body_main_menu()
        main.assert_footer_main_menu()
