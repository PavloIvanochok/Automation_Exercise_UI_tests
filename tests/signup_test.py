import allure
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


@allure.feature("Signup")
class TestSignup(BaseTest):

    @pytest.mark.order(7)
    @allure.title("T07: Successful signup with valid data.")
    @allure.description("""
    This test verifies that a new user can successfully create an account
    by providing valid registration details and that the account
    creation confirmation message is displayed.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_with_valid_data(self, delete_account):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.signup_page.open()
        self.signup_page.enter_user_name(fake.user_name)
        self.signup_page.enter_email(fake.email)
        self.signup_page.click_signup()
        self.signup_page.select_gender(fake.gender)
        self.signup_page.enter_password(fake.password)
        self.signup_page.select_day(fake.day)
        self.signup_page.select_month(fake.month)
        self.signup_page.select_year(fake.year)
        self.signup_page.enter_first_name(fake.first_name)
        self.signup_page.enter_last_name(fake.last_name)
        self.signup_page.enter_address(fake.address)
        self.signup_page.select_country(fake.country)
        self.signup_page.enter_state(fake.state)
        self.signup_page.enter_city(fake.city)
        self.signup_page.enter_zipcode(fake.zipcode)
        self.signup_page.enter_mobile_number(fake.mobile_number)
        self.signup_page.click_create_account()
        self.account_created_page.is_opened()
        self.account_created_page.verify_account_created_message()
        
    @pytest.mark.order(8)
    @allure.title("T08: Signup with an existing email.")
    @allure.description("""
    This test verifies that a new user cannot create an account
    using an email address that is already registered and that
    an appropriate error message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_with_existing_email(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.signup_page.open()
        self.signup_page.enter_user_name(fake.user_name)
        self.signup_page.enter_email(self.data.EMAIL)
        self.signup_page.click_signup()
        self.signup_page.verify_error_message()

    @pytest.mark.order(9)
    @allure.title("T09: Signup with invalid email format.")
    @allure.description("""
    This test verifies that a user cannot proceed with registration
    when entering an email address with an invalid format and that
    the appropriate email validation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_with_invalid_email(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.signup_page.open()
        self.signup_page.enter_user_name(fake.user_name)
        self.signup_page.enter_email(fake.invalid_email)
        self.signup_page.click_signup()
        self.signup_page.verify_email_validation()
        

    @pytest.mark.order(10)
    @allure.title("T10: Signup with empty name field.")
    @allure.description("""
    This test verifies that a user cannot proceed with registration
    when the name field is left empty and that the appropriate
    name validation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_without_name(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.signup_page.open()
        self.signup_page.enter_email(fake.email)
        self.signup_page.click_signup()
        self.signup_page.verify_name_validation()
        

    @pytest.mark.order(11)
    @allure.title("T11: Signup with empty email field.")
    @allure.description("""
    This test verifies that a user cannot proceed with registration
    when the email field is left empty and that the appropriate
    email validation message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_signup_without_email(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.signup_page.open()
        self.signup_page.enter_user_name(fake.user_name)
        self.signup_page.click_signup()
        self.signup_page.verify_email_validation()
