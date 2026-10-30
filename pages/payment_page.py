import os
import allure
from pathlib import Path
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support.ui import WebDriverWait


class PaymentPage(BasePage):

    PAGE_URL = Links.PAYMENT_PAGE

    NAME_ON_CARD_FIELD = ("xpath", "//input[@data-qa='name-on-card']")
    CARD_NUMBER_FIELD = ("xpath", "//input[@data-qa='card-number']")
    CVC_FIELD = ("xpath", "//input[@data-qa='cvc']")
    EXPIRY_MONTH_FIELD = ("xpath", "//input[@data-qa='expiry-month']")
    EXPIRY_YEAR_FIELD = ("xpath", "//input[@data-qa='expiry-year']")
    CONFIRM_ORDER_BUTTON = ("xpath", "//button[@data-qa='pay-button']")
    ORDER_PLACED_HEAD = ("xpath", "//h2[@data-qa='order-placed']")
    SUCCESS_MESSAGE = ("xpath", "//div[@class='col-sm-9 col-sm-offset-1']/p")
    DOWNLOAD_BUTTON = ("xpath", "//a[@class='btn btn-default check_out']")

    @allure.step("Fill card info.")
    def fill_card_info(self, card_data):
        self.enter_text(self.NAME_ON_CARD_FIELD, card_data["name_on_card"])
        self.enter_text(self.CARD_NUMBER_FIELD, card_data["card_number"])
        self.enter_text(self.CVC_FIELD, card_data["cvc"])
        self.enter_text(self.EXPIRY_MONTH_FIELD, card_data["expiry_month"])
        self.enter_text(self.EXPIRY_YEAR_FIELD, card_data["expiry_year"])

    @allure.step("Click Confirm Order button.")
    def click_confirm_order_button(self):
        self.click_element(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Verify order confirmation.")
    def verify_order_confirmation(self):
        self.wait_for_visibility(self.ORDER_PLACED_HEAD)
        message = self.wait_for_visibility(self.SUCCESS_MESSAGE)
        assert message.text == "Congratulations! Your order has been confirmed!", \
            f"Unexpected confirmation message: {message.text}"

    @allure.step("Download invoice.")
    def download_invoice(self):
        self.click_element(self.DOWNLOAD_BUTTON)

    @allure.step("Verify invoice file.")
    def verify_invoice_file(self):
        downloads_dir = Path(os.getcwd()) / "downloads"
        invoice_path = downloads_dir / "invoice.txt"
        WebDriverWait(self.driver, 10).until(
            lambda _: (
                invoice_path.exists()
                and invoice_path.stat().st_size > 0
                and not list(downloads_dir.glob("*.crdownload"))))

    @allure.step("Verify invoice content.")
    def verify_invoice_content(self, price):
        invoice_path = Path(os.getcwd()) / "downloads" / "invoice.txt"
        text = invoice_path.read_text(encoding="utf-8")
        normalized_price = price.removeprefix("Rs. ")
        assert text == f"Hi User Test, Your total purchase amount is {normalized_price}. Thank you", \
            "Unexpected invoice content!"
    