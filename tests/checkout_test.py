import pytest
import allure
from test_data.test_data import TestData
from utils.fake_data_generator import FakeDataGenerator
from base.base_test import BaseTest


@allure.feature("Checkout")
class TestCheckout(BaseTest):

    @pytest.mark.order(26)
    @allure.title("T26: Complete purchase flow.")
    @allure.description("""
    This test verifies that a logged-in user can complete the purchase
    flow by adding a product to the cart, proceeding to checkout,
    providing payment details, and confirming the order successfully.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_purchase_flow(self, logged_in_driver):
        # Test data preparation:
        data = TestData()
        fake = FakeDataGenerator()
        product_name = data.product["name"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.click_proceed_to_checkout_button()
        self.checkout_page.is_opened()
        self.checkout_page.add_comment(fake.comment)
        self.checkout_page.click_place_order_button()
        self.payment_page.is_opened()
        self.payment_page.fill_card_info(data.card_data)
        self.payment_page.click_confirm_order_button()
        self.payment_page.verify_order_confirmation()

    @pytest.mark.order(27)
    @allure.title("T27: Verify delivery address details in checkout.")
    @allure.description("""
    This test verifies that the delivery address displayed during checkout
    matches the address details provided when the user account was created.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_address_details_in_checkout(self, new_user_created, delete_account):
        # Test data preparation:
        user_details = new_user_created
        data = TestData()
        product_name = data.product["name"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.click_proceed_to_checkout_button()
        self.checkout_page.is_opened()
        self.checkout_page.verify_delivery_details(user_details)
        
    @pytest.mark.order(28)
    @allure.title("T28: Download and verify invoice after purchase.")
    @allure.description("""
    This test verifies that a logged-in user can complete a purchase,
    download the invoice, and verify that the downloaded file contains
    the expected product price.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_download_and_verify_invoice(self,clean_downloads_directory,logged_in_driver):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_price = data.product["price"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.click_proceed_to_checkout_button()
        self.checkout_page.is_opened()
        self.checkout_page.click_place_order_button()
        self.payment_page.is_opened()
        self.payment_page.fill_card_info(data.card_data)
        self.payment_page.click_confirm_order_button()
        self.payment_page.download_invoice()
        self.payment_page.verify_invoice_file()
        self.payment_page.verify_invoice_content(product_price)