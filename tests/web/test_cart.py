import time

import pytest
import allure
from my_shop_project_test.pages.cart_page import cart
from my_shop_project_test.pages.main_page import main


@allure.epic('WEB.Add product to cart')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking whether a product has been added to cart")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestCart:

    @allure.title("Adding and removing a book to cart")
    def test_item_add_and_delete_cart(self):
        main.open_shop_page()
        cart.find_item()
        time.sleep(1)
        cart.open_page_item()
        time.sleep(1)
       # cart.click_add_to_cart()
        # cart.open_cart()
        #
        # cart.clear_cart()
        # cart.confirm_clear_cart()
        #
        # cart.assert_page_cart()
