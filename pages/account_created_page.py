import allure
from base.base_page import BasePage
from config.links import Links


class AccountCreatedPage(BasePage):

    PAGE_URL = Links.ACCOUNT_CREATED_PAGE

    ACCOUNT_CREATED_MESSAGE = ("xpath", "//h2[@data-qa='account-created']")

    @allure.step("Verify account creation success message.")
    def verify_account_created_message(self):
        message = self.wait_for_visibility(self.ACCOUNT_CREATED_MESSAGE)
        assert message.text == "ACCOUNT CREATED!", \
            f"Expected account creation message: ACCOUNT CREATED! But got: '{message.text}'."
