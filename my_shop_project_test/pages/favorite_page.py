import time
import allure
from selene import browser, have

class FavoritePage:

    @allure.step("Number book search")
    def find_item(self):
        #with allure.step("Number book search"):
        browser.element('.header__search input').type(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ).press_enter()
        time.sleep(4)
        # browser.element('.header__search input').with_(timeout=200).should(have.value(
        #         "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"))
        return self

    @allure.step("Open product page")
    def open_page_item(self):
        #with allure.step("Open product page"):
        browser.element('.item .item__title').click()
        browser.element('[class="option active"]').with_(timeout=200).should(have.text("соответствию запросу"))
        return self

    @allure.step("Click add to favorites")
    def click_add_to_favorites(self):
        #with allure.step("Click add to favorites"):
        browser.element('.form-control .is-heart').click()
       # browser.element('.favorite .badge').with_(timeout=200).should(have.exact_text('1'))
        browser.element('[to="#reviews"] [class="md:block"]').with_(timeout=50).should(
            have.text("Задать вопрос"))
        return self

    @allure.step("Open favorites")
    def open_favorites(self):
        #with allure.step("Open favorites"):
        browser.element('.header__icons .favorite').click()
        browser.element('[class="is-desktop"]').with_(timeout=200).should(have.exact_text(
                'Перенести товары в наличии в корзину'))
        return self

    @allure.step("Click delete to favorites")
    def click_delete_to_favorites(self):
        #with allure.step("Click delete to favorites"):
        browser.element('.item .is-heart').click()
        browser.element('[class="text-20"]').with_(timeout=200).should(have.exact_text(
                'Избранных товаров нет'))
        return self

favorite = FavoritePage()
