import allure
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


@allure.feature("Login")
class TestLogin(BaseTest):

    @pytest.mark.order(1)
    @allure.title("T01: Successful login with valid credentials.")
    @allure.description("""
    This test verifies that a registered user can successfully log in
    using valid email and password credentials.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_valid_credentials(self):
        # Steps:
        self.login_page.open()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.home_page.is_opened()
        self.home_page.verify_login_status()

    @pytest.mark.order(2)
    @allure.title("T02: Login with unregistered email.")
    @allure.description("""
    This test verifies that a user cannot log in using a validly formatted
    email address that is not registered on the website and that an
    appropriate error message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_unregistered_email(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.login_page.open()
        self.login_page.enter_email(fake.email)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.login_page.is_opened()
        self.login_page.verify_error_message()

    @pytest.mark.order(3)
    @allure.title("T03: Login with incorrect password.")
    @allure.description("""
    This test verifies that a user cannot log in using a registered email
    address and an incorrect password, and that an appropriate error
    message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_incorrect_password(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.login_page.open()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(fake.password)
        self.login_page.click_login()
        self.login_page.is_opened()
        self.login_page.verify_error_message()

    @pytest.mark.order(4)
    @allure.title("T04: Login with empty email field.")
    @allure.description("""
    This test verifies that a user cannot log in when the email field
    is left empty and that the appropriate validation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_email_field(self):
        # Steps:
        self.login_page.open()
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.login_page.is_opened()
        self.login_page.verify_email_validation()

    @pytest.mark.order(5)
    @allure.title("T05: Login with empty password field.")
    @allure.description("""
    This test verifies that a user cannot log in when the password field
    is left empty and that the appropriate validation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_password_field(self):
        # Steps:
        self.login_page.open()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.click_login()
        self.login_page.is_opened()
        self.login_page.verify_password_validation()
