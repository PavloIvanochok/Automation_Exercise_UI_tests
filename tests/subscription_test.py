import allure
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


@allure.feature("Subscription")
class TestSubscription(BaseTest):

    @pytest.mark.order(30)
    @allure.title("T30: Verify subscription on the home page.")
    @allure.description("""
    This test verifies that a user can subscribe to the newsletter
    from the home page by entering a valid email address and that
    the subscription success message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_subscription_on_home_page(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        email = fake.email
        # Steps:
        self.home_page.open()
        self.home_page.enter_subscription_email(email)
        self.home_page.click_subscribe()
        self.home_page.verify_subscription_success_message()
    
    @pytest.mark.order(31)
    @allure.title("T31: Verify subscription on the cart page.")
    @allure.description("""
    This test verifies that a user can subscribe to the newsletter
    from the cart page by entering a valid email address and that
    the subscription success message is displayed.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_subscription_on_cart_page(self):
        # Test data preparation:
        fake = FakeDataGenerator()
        email = fake.email
        # Steps:
        self.cart_page.open()
        self.cart_page.enter_subscription_email(email)
        self.cart_page.click_subscribe()
        self.cart_page.verify_subscription_success_message()