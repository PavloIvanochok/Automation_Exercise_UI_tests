import allure
import pytest
from base.base_test import BaseTest
from test_data.test_data import TestData


@allure.feature("Cart")
class TestCart(BaseTest):

    @pytest.mark.order(16)
    @allure.title("T16: Add product to cart and verify confirmation.")
    @allure.description("""
    This test verifies that a user can add a selected product to the cart
    and that the confirmation modal is displayed after the product
    is added successfully.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.verify_confirmation_modal()

    @pytest.mark.order(17)
    @allure.title("T17: Verify product information in cart.")
    @allure.description("""
    This test verifies that after adding a selected product to the cart,
    the product name and price are displayed correctly in the cart.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_product_info_in_cart(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_price = data.product["price"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.is_opened()
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.is_opened()
        self.cart_page.verify_product_name_and_price(product_name, product_price)

    @pytest.mark.order(18)
    @allure.title("T18: Verify product quantity and total price in cart.")
    @allure.description("""
    This test verifies that a user can set the desired product quantity
    before adding the product to the cart and that the selected quantity
    and total price are displayed correctly in the cart.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_product_quantity_and_total_price_in_cart(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_price = data.product["price"]
        quantity = data.quantity
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.is_opened()
        self.product_details_page.set_quantity(quantity)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.is_opened()
        self.cart_page.verify_quantity(product_name, quantity)
        self.cart_page.verify_total_price(product_name, product_price, quantity)

    @pytest.mark.order(19)
    @allure.title("T19: Delete product from cart.")
    @allure.description("""
    This test verifies that a user can remove a product from the cart
    and that the cart is empty after the product is deleted.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_product_from_cart(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_id = data.product["id"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.product_details_page.open_cart()
        self.cart_page.delete_product(product_id)
        self.cart_page.verify_cart_is_empty()

    @pytest.mark.order(20)
    @allure.title("T20: Add recommended product to cart.")
    @allure.description("""
    This test verifies that a user can add a recommended product
    to the cart from the home page and that the product name and price
    are displayed correctly in the cart.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product_to_cart_from_recommended_items(self):
        # Test data preparation:
        data = TestData()
        product_name = data.recommended_product["name"]
        product_price = data.recommended_product["price"]
        # Steps:
        self.home_page.open()
        self.home_page.verify_recommended_section()
        self.home_page.add_recommended_product_to_cart(product_name)
        self.home_page.open_cart()
        self.cart_page.is_opened()
        self.cart_page.verify_product_name_and_price(product_name, product_price)

    @pytest.mark.order(21)
    @allure.title("T21: Verify cart contents after login.")
    @allure.description("""
    This test verifies that a product added to the cart before login
    remains in the cart after the user logs in, and that the product
    name and price are displayed correctly.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product_and_verify_cart_after_login(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_price = data.product["price"]
        product_id = data.product["id"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.click_add_to_cart_button()
        self.login_page.open()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.home_page.is_opened()
        self.home_page.click_cart_button()
        self.cart_page.is_opened()
        self.cart_page.verify_product_name_and_price(product_name, product_price)
        # Postconditions:
        self.cart_page.delete_product(product_id)
