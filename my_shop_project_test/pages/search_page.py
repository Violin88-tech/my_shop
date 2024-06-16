import time
import allure
from selene import browser, have

class SearchPage:
    @allure.step("Input text for search positive")
    #with allure.step("Input text for search positive"):
    def header_search_positive(self):
        browser.element('.header__search input').type('Тетради').press_enter()
        browser.element('.header__search input').with_(timeout=200).should(have.value('Тетради'))

    @allure.step("Input text for search negative")
    #with allure.step("Input text for search negative"):
    def header_search_negative(self):
        browser.element('.header__search input').type('asddfgrhtjykykk8967868686').press_enter()

search = SearchPage()
