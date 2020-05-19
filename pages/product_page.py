from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def compare_name(self):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME).text
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        assert alert_name == name, "The name in the basket does not match"

    def compare_price(self):
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert alert_price == price, "The price in the basket does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Successful message does not disappear"


