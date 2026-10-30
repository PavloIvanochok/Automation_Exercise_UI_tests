import allure
from base.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    LOGIN_FORM = ("xpath", "//div[@class='login-form']")
    EMAIL_FIELD = ("xpath", "//input[@data-qa='login-email']")
    PASSWORD_FIELD = ("xpath", "//input[@data-qa='login-password']")
    LOGIN_BUTTON = ("xpath", "//button[@data-qa='login-button']")
    ERROR_MESSAGE = ("xpath", "//p[@style='color: red;']")

    @allure.step("Enter email.")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Enter password.")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("Click Login button.")
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Verify login error message.")
    def verify_error_message(self):
        error_message = self.wait_for_visibility(self.ERROR_MESSAGE)
        assert error_message.text == "Your email or password is incorrect!", \
            f"Expected error message: Your email or password is incorrect!, but got '{error_message.text}'."

    @allure.step("Verify password field validation is triggered.")
    def verify_password_validation(self):
        message = self.get_validation_message(self.PASSWORD_FIELD)
        assert message, \
            "Expected browser validation message for the password field, but the message was empty."

    @allure.step("Verify email field validation is triggered.")
    def verify_email_validation(self):
        message = self.get_validation_message(self.EMAIL_FIELD)
        assert message, \
            "Expected browser validation message for the email field, but the message was empty."

    @allure.step("Verify login form is displayed after logout.")
    def verify_logout_status(self):
        self.wait_for_visibility(self.LOGIN_FORM)
