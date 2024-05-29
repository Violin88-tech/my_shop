import pytest
import allure
from my_shop_project_test.pages.main_page import main
from my_shop_project_test.pages.search_page import search


@allure.epic('WEB.Search Page')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking an successful and an unsuccessful search")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestSearch:

    @allure.title("Ckeck with positive search")
    def test_header_search_positive(self):
        main.open_shop_page()
        search.header_search_positive()
        search.search_result_success()

    @allure.title("Ckeck with negative search")
    def test_header_search_negative(self):
        main.open_shop_page()
        search.header_search_negative()
        search.search_result_failure()
