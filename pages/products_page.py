import allure
from base.base_page import BasePage
from config.links import Links


class ProductsPage(BasePage):

    PAGE_URL = Links.PRODUCTS_PAGE

    PRODUCTS_SECTION = ("xpath", "//div[@class='features_items']")
    PRODUCTS = ("xpath", ".//div[@class='col-sm-4']")
    SEARCH_FIELD = ("xpath", "//input[@id='search_product']")
    SEARCH_BUTTON = ("xpath", "//button[@id='submit_search']")
    SEARCH_RESULT_HEAD = ("xpath", "//h2[@class='title text-center']")
    FILTERED_SECTION_HEAD = ("xpath", "//div[@class='features_items']/h2")

    @allure.step("Verify that products are displayed.")
    def verify_products_displayed(self):
        products_section = self.wait_for_visibility(self.PRODUCTS_SECTION)
        products = products_section.find_elements(*self.PRODUCTS)
        assert products, "No products are displayed."

    @allure.step("Select product by name.")
    def select_product_by_name(self, product_name):
        select_product_button = (
            "xpath", f"//p[text()='{product_name}']/ancestor::div[@class='product-image-wrapper']//div[@class='choose']//a")
        button = self.wait_for_visibility(select_product_button)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Enter product name in search.")
    def enter_product_name(self, product_name):
        self.enter_text(self.SEARCH_FIELD, product_name)

    @allure.step("Click Search button.")
    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    @allure.step("Verify product in search results.")
    def verify_product_in_search_results(self, product_id):
        self.wait_for_visibility(self.SEARCH_RESULT_HEAD)
        self.wait_for_visibility(("xpath", f"//a[@data-product-id='{product_id}']"))

    @allure.step("Filter products by brand.")
    def filter_by_brand(self, brand_name):
        brand_filter = ("xpath", f"//a[@href='/brand_products/{brand_name}']")
        element = self.wait_for_visibility(brand_filter)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Choose category and subcategory.")
    def choose_category_and_subcategory(self, category_name, subcategory_name):
        category = ("xpath", f"//a[@href='#{category_name}']")
        self.click_element(category)
        subcategory = ("xpath", f"//div[@id='{category_name}']//a[text()='{subcategory_name} ']")
        self.click_element(subcategory)

    @allure.step("Verify that no products are found.")
    def verify_no_products_found(self):
        products = self.driver.find_elements("xpath", "//div[@class='single-products']")
        assert len(products) == 0, \
            f"Expected no products for the search query, but found {len(products)} product(s)."
