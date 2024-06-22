import allure
from selene import browser, have

class MainPage:
    @allure.step("Open marketplace")
    #with allure.step("Open marketplace"):
    def open_shop_page(self):
        browser.open('/')
        browser.element('[href*="/my/partner"]').with_(timeout=150).should(have.text('Партнёрам'))
        return self

    @allure.step("Checking first level menu items")
    #with allure.step("Checking first level menu items"):
    def assert_header_main_menu(self):
        browser.element('[href*="/my/partner"]').with_(timeout=150).should(have.text('Партнёрам'))
        return self

    @allure.step("Checking second level menu items")
    #with allure.step("Checking second level menu items"):
    def assert_body_main_menu(self):
        browser.element('[aria-label="Майшоп.Гид рекомендует"]').with_(timeout=150).should(
                have.text('Майшоп.Гид рекомендует'))
        return self

    @allure.step("Checking third level menu items")
    #with allure.step("Checking third level menu items"):
    def assert_footer_main_menu(self):
        browser.element('.footer .footer__copyright').with_(timeout=160).should(
                have.text('Все права защищены © 2002-2024 Майшоп'))
        return self


main = MainPage()