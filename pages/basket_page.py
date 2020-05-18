from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def product_not_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET),\
            'The product is in the basket, but should not be'

    def should_be_message_basket_is_empty(self):
        text_massage = 'Your basket is empty. Continue shopping'
        massage = self.browser.find_element(*BasketPageLocators.MESSAGE).text
        assert massage == text_massage, "There is no message that the basket is empty"
