import allure
from base.base_page import BasePage
from config.links import Links


class CartPage(BasePage):

    PAGE_URL = Links.CART_PAGE

    EMPTY_CART_MESSAGE = ("xpath", "//span[@id='empty_cart']/p/b")
    PROCEED_TO_CHECKOUT_BUTTON = ("xpath", "//a[@class='btn btn-default check_out']")
    SUBSCRIPTION_INPUT = ("xpath", "//input[@id='susbscribe_email']")
    SUBSCRIPTION_BUTTON = ("xpath", "//button[@type='submit']")
    SUCCESS_SUBSCRIPTION_MESSAGE = ("xpath", "//div[@id='success-subscribe']/div")

    @allure.step("Verify product name and price.")
    def verify_product_name_and_price(self, product_name, price):
        self.wait_for_visibility(("xpath", f"//a[text()='{product_name}']"))
        price_value = self.wait_for_visibility(
            ("xpath", f"//a[text()='{product_name}']/ancestor::tr//td[@class='cart_price']/p"))
        assert price_value.text == price, \
            f"Expected product price: '{price}', but got: '{price_value.text}'."

    @allure.step("Verify product quantity.")
    def verify_quantity(self, product_name, quantity):
        quantity_info = self.wait_for_visibility(
            ("xpath", f"//a[text()='{product_name}']/ancestor::tr//td[@class='cart_quantity']/button"))
        assert int(quantity_info.text) == quantity, \
            f"Expected quantity {quantity}, but got {quantity_info.text}"

    @allure.step("Verify total price.")
    def verify_total_price(self, product_name, price, quantity):
        total_info = self.wait_for_visibility(
            ("xpath", f"//a[text()='{product_name}']/ancestor::tr//p[@class='cart_total_price']"))
        total_value = int(total_info.text.replace("Rs.", "").strip())
        price_value = int(price.replace("Rs.", "").strip())
        assert total_value == price_value * quantity, \
            f"Expected total {price_value * quantity}, but got {total_value}"

    @allure.step("Delete product from cart.")
    def delete_product(self, product_id):
        self.click_element(("xpath", f"//td[@class='cart_delete']/a[@data-product-id='{product_id}']"))

    @allure.step("Verify that cart is empty.")
    def verify_cart_is_empty(self):
        message = self.wait_for_visibility(self.EMPTY_CART_MESSAGE)
        assert message.text == "Cart is empty!", f"Unexpected cart message: {message.text}"

    @allure.step("Click Proceed To Checkout button.")
    def click_proceed_to_checkout_button(self):
        self.click_element(self.PROCEED_TO_CHECKOUT_BUTTON)

    @allure.step("Enter subscription email.")
    def enter_subscription_email(self, email):
        subscription_input = self.wait_for_visibility(self.SUBSCRIPTION_INPUT)
        subscription_input.clear()
        subscription_input.send_keys(email)

    @allure.step("Click Subscribe button.")
    def click_subscribe(self):
        self.click_element(self.SUBSCRIPTION_BUTTON)

    @allure.step("Verify subscription success message.")
    def verify_subscription_success_message(self):
        success_message = self.wait_for_visibility(self.SUCCESS_SUBSCRIPTION_MESSAGE)
        assert "You have been successfully subscribed!" == success_message.text, \
            f"Expected 'You have been successfully subscribed!', but got '{success_message.text}'"
