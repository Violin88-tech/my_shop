import time

import pytest
import allure
from my_shop_project_test.pages.favorite_page import favorite
from my_shop_project_test.pages.main_page import main


@allure.epic('WEB.Add product to favorites')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking whether a product has been added to favorites")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestFavorites:

    @allure.title("Adding and removing a book to favorites")
    def test_item_add_and_delete_favorites(self):
        main.open_shop_page()
        time.sleep(1)
        favorite.find_item()
        favorite.open_page_item()
        favorite.click_add_to_favorites()
        # time.sleep(1)
        favorite.open_favorites()
        favorite.click_delete_to_favorites()
        #
      #  favorite.assert_page_favorites()
