from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items are presented, but should not be"

    def should_be_empty_basket_message(self):
        a = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert a is "Ваша корзина пуста" or "Your basket is empty.", \
            "Wrong message; basket is not empty"
