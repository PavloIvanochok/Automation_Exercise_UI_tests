import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Account Management")
class TestDeleteAccount(BaseTest):

    @pytest.mark.order(12)
    @allure.title("T12: Successful account deletion.")
    @allure.description("""
    This test verifies that a registered user can successfully delete
    their account and that the account deletion confirmation message
    is displayed.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_account(self, new_user_created):
        # Steps:
        self.home_page.open()
        self.home_page.click_delete_account()
        self.home_page.verify_account_deleted_message()
