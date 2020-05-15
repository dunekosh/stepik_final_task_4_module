from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    ALERT_NAME = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')

