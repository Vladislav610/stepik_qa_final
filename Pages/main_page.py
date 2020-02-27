from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators


class MainPage(BasePage):
    def should_be_go_to_basket(self):
        button_go_to_basket = self.browser.find_element(*MainPageLocators.BUTTON_GO_TO_BASKET)
        button_go_to_basket.click()




