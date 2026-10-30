import allure
import pytest
from base.base_test import BaseTest
from test_data.test_data import TestData
from utils.fake_data_generator import FakeDataGenerator


@allure.feature("Products")
class TestProducts(BaseTest):

    @pytest.mark.order(13)
    @allure.title("T13: Verify products page is displayed.")
    @allure.description("""
    This test verifies that a user can navigate to the products page
    and that the products are displayed correctly.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_products_page(self):
        # Steps:
        self.home_page.open()
        self.home_page.click_products_button()
        self.products_page.is_opened()
        self.products_page.verify_products_displayed()

    @pytest.mark.order(14)
    @allure.title("T14: Verify product details.")
    @allure.description("""
    This test verifies that a user can open a product details page
    for a selected product and that the product name, photo, category,
    price, and quantity are displayed correctly.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_product_details(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.is_opened()
        self.product_details_page.verify_product_name_displayed()
        self.product_details_page.verify_product_photo_displayed()
        self.product_details_page.verify_product_category_displayed()
        self.product_details_page.verify_product_price_displayed()
        self.product_details_page.verify_product_quantity_displayed()

    @pytest.mark.order(15)
    @allure.title("T15: Submit a review for a product.")
    @allure.description("""
    This test verifies that a user can submit a review for a selected
    product by providing their name, email, and review text, and that
    the review submission confirmation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_write_review_for_product(self):
        # Test data preparation:
        data = TestData()
        fake = FakeDataGenerator()
        product_name = data.product["name"]
        # Steps:
        self.products_page.open()
        self.products_page.select_product_by_name(product_name)
        self.product_details_page.verify_review_section_displayed()
        self.product_details_page.enter_user_name(fake.first_name)
        self.product_details_page.enter_user_email(fake.email)
        self.product_details_page.enter_review(fake.review)
        self.product_details_page.submit_review()
        self.product_details_page.verify_review_submission_message()
    