from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, 'header .basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#content_inner .input-group')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    PASSWORD1 = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    PASSWORD2 = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button[name="registration_submit"]')


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    ALERT_NAME = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')

