import time

import allure
from selene import browser, have


class SearchPage:
    with allure.step("Input text for search positive"):
        def header_search_positive(self):
            browser.element('.header__search input').type('Тетради').press_enter()
           # time.sleep(2)
    #
    # with allure.step("Check the result of an successful search"):
    #     def search_result_success(self):
    #         browser.element('.h1 .title').should(have.text('Тетради'))
    #
    with allure.step("Input text for search negative"):
        def header_search_negative(self):
            browser.element('.header__search input').type('asddfgrhtjykykk8967868686').press_enter()
    #
    # with allure.step("Check the result of an unsuccessful search"):
    #     def search_result_failure(self):
    #         browser.element('.search-type__text').should(have.text('По вашему запросу ничего не найдено. Возможно, вам понравятся эти популярные товары'))
    #

search = SearchPage()
