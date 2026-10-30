import allure
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


@allure.feature("Contact Us")
class TestContactUs(BaseTest):

    @pytest.mark.order(29)
    @allure.title("T29: Submit the contact us form.")
    @allure.description("""
    This test verifies that a user can submit the contact us form
    by providing their name, email, subject, and message, uploading
    a file, and confirming the submission alert.
    The success confirmation message should be displayed afterward.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_submit_contact_us_form(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        # Steps:
        self.contact_us_page.open()
        self.contact_us_page.is_opened()
        self.contact_us_page.enter_name(fake.first_name)
        self.contact_us_page.enter_email(fake.email)
        self.contact_us_page.enter_subject(fake.subject)
        self.contact_us_page.enter_message(fake.message)
        self.contact_us_page.upload_test_file()
        self.contact_us_page.click_submit()
        self.contact_us_page.approve_alert()
        self.contact_us_page.verify_success_message()
        