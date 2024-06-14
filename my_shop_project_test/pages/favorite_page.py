import time
import allure
from selene import browser, have

class FavoritePage:
    with allure.step("Number book search"):
        def find_item(self):
            browser.element('.header__search input').type(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ).press_enter()
            browser.element('.header__search input').with_(timeout=200).should(have.value(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"))
            return self

    with allure.step("Open product page"):
        def open_page_item(self):
            browser.element('.item .item__title').click()
            browser.element('[to="#reviews"] [class="md:block"]').with_(timeout=50).should(have.text("Задать вопрос"))
            return self

    with allure.step("Click add to favorites"):
        def click_add_to_favorites(self):
            browser.element('.form-control .is-heart').click()
            browser.element('.favorite .badge').with_(timeout=200).should(have.exact_text('1'))
            return self

    with allure.step("Open favorites"):
        def open_favorites(self):
            browser.element('.header__icons .favorite').click()
            browser.element('[class="is-desktop"]').with_(timeout=200).should(have.exact_text(
                'Перенести товары в наличии в корзину'))
            return self

    with allure.step("Click delete to favorites"):
        def click_delete_to_favorites(self):
            browser.element('.item .is-heart').click()
            time.sleep(3)
            return self

favorite = FavoritePage()
