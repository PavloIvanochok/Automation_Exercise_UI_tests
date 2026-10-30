import allure
import pytest
from base.base_test import BaseTest
from test_data.test_data import TestData


@allure.feature("Search and Filter")
class TestSearchFilter(BaseTest):

    @pytest.mark.order(22)
    @allure.title("T22: Search product by name.")
    @allure.description("""
    This test verifies that a user can search for a product by name
    and that the expected product is displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_product(self):
        # Test data preparation:
        data = TestData()
        product_name = data.product["name"]
        product_id = data.product["id"]
        # Steps:
        self.products_page.open()
        self.products_page.enter_product_name(product_name)
        self.products_page.click_search_button()
        self.products_page.verify_product_in_search_results(product_id)

    @pytest.mark.order(23)
    @allure.title("T23: Search for a non-existent product.")
    @allure.description("""
    This test verifies that searching for a product that does not exist
    in the catalog returns no matching products and displays the
    appropriate no-results state.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_non_existent_product(self):
        # Test data preparation:
        data = TestData()
        non_existent_product = data.non_existent_product
        # Steps:
        self.products_page.open()
        self.products_page.enter_product_name(non_existent_product)
        self.products_page.click_search_button()
        self.products_page.verify_no_products_found()

    @pytest.mark.order(24)
    @allure.title("T24: Filter products by brand.")
    @allure.description("""
    This test verifies that a user can filter products by a selected brand,
    that the corresponding brand products page is displayed, and that
    all displayed products belong to the selected brand.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_products_by_brand(self):
        # Test data preparation:
        data = TestData()
        brand = data.brand
        # Steps:
        self.products_page.open()
        self.products_page.filter_by_brand(brand)
        self.brand_products_page.is_opened()
        self.brand_products_page.verify_filtered_section_displayed(brand)
        self.brand_products_page.verify_each_product_belongs_to_brand(brand)
        
    @pytest.mark.order(25)
    @allure.title("T25: Filter products by category and subcategory.")
    @allure.description("""
    This test verifies that a user can select a product category
    and subcategory and that all displayed products belong to
    the selected category and subcategory.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_products_by_category_subcategory(self):
        # Test data preparation:
        data = TestData()
        category = data.category
        subcategory = data.subcategory
        # Steps:
        self.products_page.open()
        self.products_page.choose_category_and_subcategory(category, subcategory)
        self.products_category_page.is_opened()
        self.products_category_page.verify_each_product_belongs_to_category_and_subcategory(category,subcategory)