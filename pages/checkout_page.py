import allure
from base.base_page import BasePage
from config.links import Links


class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    COMMENT_FIELD = ("xpath", "//textarea[@name='message']")
    PLACE_ORDER_BUTTON = ("xpath", "//a[@href='/payment']")
    DELIVERY_DETAILS_NAME = ("xpath", "//ul[@id='address_delivery']//li[contains(@class, 'address_firstname')]")
    DELIVERY_DETAILS_ADDRESS = ("xpath", "(//ul[@id='address_delivery']//li[@class='address_address1 address_address2'])[2]")
    DELIVERY_DETAILS_CITY_STATE_ZIP = ("xpath", "//ul[@id='address_delivery']//li[contains(@class, 'address_city')]")
    DELIVERY_DETAILS_COUNTRY = ("xpath", "//ul[@id='address_delivery']//li[contains(@class, 'address_country_name')]")
    DELIVERY_DETAILS_PHONE = ("xpath", "//ul[@id='address_delivery']//li[contains(@class, 'address_phone')]")

    @allure.step("Add a comment about your order.")
    def add_comment(self, comment):
        self.enter_text(self.COMMENT_FIELD, comment)

    @allure.step("Click Place Order button.")
    def click_place_order_button(self):
        self.click_element(self.PLACE_ORDER_BUTTON)

    @allure.step("Verify delivery details on checkout page.")
    def verify_delivery_details(self, user_details):
        name = self.wait_for_visibility(self.DELIVERY_DETAILS_NAME).text
        expected_name = f"{user_details.gender}. {user_details.first_name} {user_details.last_name}"
        assert name == expected_name, \
            f"Expected name: '{expected_name}', but got: '{name}'"

        address = self.wait_for_visibility(self.DELIVERY_DETAILS_ADDRESS).text
        assert address == user_details.address, \
            f"Expected address: '{user_details.address}', but got: '{address}'"

        city_state_zip = self.wait_for_visibility(self.DELIVERY_DETAILS_CITY_STATE_ZIP).text
        expected_city_state_zip = f"{user_details.city} {user_details.state} {user_details.zipcode}"
        assert city_state_zip == expected_city_state_zip, \
            f"Expected city/state/zip: '{expected_city_state_zip}', but got: '{city_state_zip}'"

        country = self.wait_for_visibility(self.DELIVERY_DETAILS_COUNTRY).text
        assert country == user_details.country, \
            f"Expected country: '{user_details.country}', but got: '{country}'"

        phone = self.wait_for_visibility(self.DELIVERY_DETAILS_PHONE).text
        assert phone == user_details.mobile_number, \
            f"Expected phone: '{user_details.mobile_number}', but got: '{phone}'"
