from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_to_basket.click()

    def should_be_correct_name(self):
        a = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT_NAME).text
        b = self.browser.find_element(*ProductPageLocators.FACT_PRODUCT_NAME).text
        assert a == b, "Names are different!"

    def should_be_correct_price(self):
        a = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT_PRICE).text
        b = self.browser.find_element(*ProductPageLocators.FACT_PRODUCT_PRICE).text
        assert a == b, "Prices are different!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
