import time
from selene import browser, have, by
import allure
class CartPage:

        @allure.step("Book search")
        def find_item(self):
            browser.element(".header__search input").type(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ).press_enter()
            browser.element(".header__search input").with_(timeout=200).should(have.value(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ))
            return self

        @allure.step("Open product page")
        def open_page_item(self):

            #with allure.step("Open product page"):
            browser.element('.item .item__title').click()
            browser.element('[to="#reviews"] [class="md:block"]').with_(timeout=50).should(
                        have.text("Задать вопрос"))
            return self

        @allure.step("Click add to cart")
        def click_add_to_cart(self):

           #with allure.step("Click add to cart"):
            browser.element('.form-control>.field.flex-grow>button').click()
            browser.element('[href="/my/cart"] .badge').with_(timeout=100).should(have.exact_text('1'))
            return self

        @allure.step("Open cart")
        def open_cart(self):
           #with allure.step("Open cart"):
            browser.element('[href="/my/cart"]').click()
            browser.element('[class="cart-sort-pane__control"]').with_(timeout=50).should(have.text("Выбрать всё"))
            return self

        @allure.step("Clear cart")
        def clear_cart(self):
         #  with allure.step("Clear cart"):
            browser.element('.cart-item .icon__delete').click()
            browser.element(".h2").with_(timeout=50).should(have.text("Удаление товаров"))
            return self

        @allure.step("Confirm clear cart")
        def confirm_clear_cart(self):
         # with allure.step("Confirm clear cart"):
            browser.element(' .popup-modal .cart-confirm__btns').element(by.text('Удалить')).click()
            browser.element('.wrap h3').with_(timeout=50).should(have.text('Ваша корзина пуста'))
            return self

cart = CartPage()
