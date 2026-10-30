import allure
from base.base_page import BasePage
from config.links import Links


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    LOGIN_STATUS = ("xpath", "//i[@class='fa fa-user']")
    LOGOUT_BUTTON = ("xpath", "//a[@href='/logout']")
    PRODUCTS_BUTTON = ("xpath", "//a[@href='/products']")
    CART_BUTTON = ("xpath", "//ul[@class='nav navbar-nav']//a[@href='/view_cart']")
    RECOMMENDED_SECTION = ("xpath", "//div[@id='recommended-item-carousel']")
    VIEW_CART_BUTTON = ("xpath", "//a[@href='/view_cart']/u")
    DELETE_ACCOUNT_BUTTON = ("xpath", "//a[@href='/delete_account']")
    ACCOUNT_DELETED_MESSAGE = ("xpath", "//h2[@data-qa='account-deleted']/b")
    SUBSCRIPTION_INPUT = ("xpath", "//input[@id='susbscribe_email']")
    SUBSCRIPTION_BUTTON = ("xpath", "//button[@type='submit']")
    SUCCESS_SUBSCRIPTION_MESSAGE = ("xpath", "//div[@id='success-subscribe']/div")

    @allure.step("Verify successful login.")
    def verify_login_status(self):
        self.wait_for_visibility(self.LOGIN_STATUS)

    @allure.step("Click Logout button.")
    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    @allure.step("Click Products button.")
    def click_products_button(self):
        button = self.wait_for_visibility(self.PRODUCTS_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Click Cart button.")
    def click_cart_button(self):
        self.click_element(self.CART_BUTTON)

    @allure.step("Verify recommended section.")
    def verify_recommended_section(self):
        self.wait_for_visibility(self.RECOMMENDED_SECTION)

    @allure.step("Add product from recommended items to cart.")
    def add_recommended_product_to_cart(self, product_name):
        product = self.wait_for_visibility(
            ("xpath", f"//div[@class='recommended_items']//p[text()='{product_name}']/following-sibling::a"))
        self.driver.execute_script("arguments[0].click();", product)

    @allure.step("Open cart.")
    def open_cart(self):
        self.click_element(self.VIEW_CART_BUTTON)

    @allure.step("Click Delete Account button.")
    def click_delete_account(self):
        button = self.wait_for_visibility(self.DELETE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Verify account deleted message.")
    def verify_account_deleted_message(self):
        message = self.wait_for_visibility(self.ACCOUNT_DELETED_MESSAGE)
        assert message.text == "ACCOUNT DELETED!", \
            f"Expected 'ACCOUNT DELETED!', but got '{message.text}'"

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
