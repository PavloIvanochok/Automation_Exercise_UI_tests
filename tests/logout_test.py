import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Logout")
class TestLogout(BaseTest):

    @pytest.mark.order(6)
    @allure.title("T06: Successful logout.")
    @allure.description("""
    This test verifies that a logged-in user can successfully log out
    and is redirected to the login page.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout(self, logged_in_driver):
        # Steps:
        self.home_page.is_opened()
        self.home_page.click_logout()
        self.login_page.is_opened()
        self.login_page.verify_logout_status()
