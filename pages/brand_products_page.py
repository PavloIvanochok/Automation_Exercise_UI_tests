import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class BrandProductsPage(BasePage):

    PAGE_URL = Links.BRAND_PRODUCTS_PAGE

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Verify filtered section is displayed.")
    def verify_filtered_section_displayed(self, brand_name):
        self.wait_for_visibility(("xpath", f"//div[@class='features_items']/h2[text()='Brand - {brand_name} Products']"))

    @allure.step("Verify each product belongs to brand.")
    def verify_each_product_belongs_to_brand(self, brand_name):
        product_locator = ("xpath", "//div[@class='features_items']/div[@class='col-sm-4']")
        products = self.driver.find_elements(*product_locator)
        assert products, "No products found for selected brand."
        for index in range(len(products)):
            products = self.driver.find_elements(*product_locator)
            product = products[index]
            view_product_button = product.find_element("xpath", ".//div[@class='choose']//a")
            self.driver.execute_script("arguments[0].click();", view_product_button)
            self.wait_for_visibility(("xpath", f"//div[@class='product-information']/p[contains(., '{brand_name}')]"))
            self.driver.back()
