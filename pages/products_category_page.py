import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductsCategoryPage(BasePage):

    PAGE_URL = Links.PRODUCTS_CATEGORY_PAGE

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Verify each product belongs to category and subcategory.")
    def verify_each_product_belongs_to_category_and_subcategory(self, category_name, subcategory_name):
        products_locator = ("xpath", "//div[@class='features_items']/div[@class='col-sm-4']")
        products = self.driver.find_elements(*products_locator)
        assert products, "No products found for selected category and subcategory."
        for index in range(len(products)):
            products = self.driver.find_elements(*products_locator)
            product = products[index]
            view_product_button = product.find_element("xpath", ".//div[@class='choose']//a")
            self.driver.execute_script("arguments[0].click();", view_product_button)
            self.wait_for_visibility(
                ("xpath", f"//div[@class='product-information']/p[contains(., '{category_name}') and contains(., '{subcategory_name}')]"))
            self.driver.back()
