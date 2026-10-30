import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage(BasePage):

    PAGE_URL = Links.PRODUCT_DETAILS_PAGE

    PRODUCT_NAME = ("xpath", "//div[@class='product-information']/h2")
    PRODUCT_PHOTO = ("xpath", "//div[@class='view-product']/img")
    PRODUCT_CATEGORY = ("xpath", "(//div[@class='product-information']/p)[1]")
    PRODUCT_PRICE = ("xpath", "//div[@class='product-information']/span/span")
    PRODUCT_QUANTITY = ("xpath", "//input[@id='quantity']")
    ADD_TO_CART_BUTTON = ("xpath", "//button[@class='btn btn-default cart']")
    CONFIRMATION_MODAL = ("xpath", "//div[@class='modal-content']")
    CONFIRMATION_STATUS = ("xpath", "//div[@class='modal-content']//h4")
    VIEW_CART = ("xpath", "//a[@href='/view_cart']/u")
    USER_NAME_FIELD = ("xpath", "//input[@id='name']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    REVIEW_FIELD = ("xpath", "//textarea[@name='review']")
    SUBMIT_REVIEW_BUTTON = ("xpath", "//button[@id='button-review']")
    REVIEW_SUBMISSION_MESSAGE = ("xpath", "//div[@id='review-section']//span")
    REVIEW_SECTION = ("xpath", "//form[@id='review-form']")

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Verify that product name is displayed.")
    def verify_product_name_displayed(self):
        name = self.wait_for_visibility(self.PRODUCT_NAME)
        assert name.text, "Product name is empty."

    @allure.step("Verify that product photo is displayed.")
    def verify_product_photo_displayed(self):
        photo = self.wait_for_visibility(self.PRODUCT_PHOTO)
        assert photo.get_attribute("src"), "Product photo has no source."

    @allure.step("Verify that product category is displayed.")
    def verify_product_category_displayed(self):
        category = self.wait_for_visibility(self.PRODUCT_CATEGORY)
        assert category.text, "Product category is empty."

    @allure.step("Verify that product price is displayed.")
    def verify_product_price_displayed(self):
        price = self.wait_for_visibility(self.PRODUCT_PRICE)
        assert price.text, "Product price is empty."

    @allure.step("Verify that product quantity is displayed.")
    def verify_product_quantity_displayed(self):
        quantity = self.wait_for_visibility(self.PRODUCT_QUANTITY)
        assert quantity.get_attribute("value"), "Product quantity is empty."

    @allure.step("Click Add to cart button.")
    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Verify that the add-to-cart confirmation modal appears.")
    def verify_confirmation_modal(self):
        self.wait_for_visibility(self.CONFIRMATION_MODAL)
        status = self.wait_for_visibility(self.CONFIRMATION_STATUS)
        assert status.text == "Added!", "Unexpected confirmation status."

    @allure.step("Open cart.")
    def open_cart(self):
        self.click_element(self.VIEW_CART)

    @allure.step("Set product quantity.")
    def set_quantity(self, quantity):
        quantity_field = self.wait_for_visibility(self.PRODUCT_QUANTITY)
        quantity_field.clear()
        self.enter_text(quantity_field, quantity)

    @allure.step("Enter user name for product review.")
    def enter_user_name(self, name):
        name_field = self.wait_for_visibility(self.USER_NAME_FIELD)
        name_field.clear()
        self.enter_text(name_field, name)

    @allure.step("Verify that the review section is displayed.")
    def verify_review_section_displayed(self):
        self.wait_for_visibility(self.REVIEW_SECTION)

    @allure.step("Enter user email for product review.")
    def enter_user_email(self, email):
        email_field = self.wait_for_visibility(self.EMAIL_FIELD)
        email_field.clear()
        self.enter_text(email_field, email)

    @allure.step("Enter product review.")
    def enter_review(self, review):
        review_field = self.wait_for_visibility(self.REVIEW_FIELD)
        review_field.clear()
        self.enter_text(review_field, review)

    @allure.step("Submit product review.")
    def submit_review(self):
        self.click_element(self.SUBMIT_REVIEW_BUTTON)

    @allure.step("Verify product review submission message.")
    def verify_review_submission_message(self):
        confirmation_message = self.wait_for_visibility(self.REVIEW_SUBMISSION_MESSAGE)
        assert "Thank you for your review." == confirmation_message.text, \
            f"Expected 'Thank you for your review.', but got '{confirmation_message.text}'"
