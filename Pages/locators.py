from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, ".hidden-xs > span > a")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    REAL_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    FACT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    FACT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators:
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")