import os
import allure
from base.base_page import BasePage
from config.links import Links


class ContactUsPage(BasePage):

    PAGE_URL = Links.CONTACT_US_PAGE

    NAME_FIELD = ("xpath", "//input[@data-qa='name']")
    EMAIL_FIELD = ("xpath", "//input[@data-qa='email']")
    SUBJECT_FIELD = ("xpath", "//input[@data-qa='subject']")
    MESSAGE_FIELD = ("xpath", "//textarea[@data-qa='message']")
    UPLOAD_FILE_FIELD = ("xpath", "//input[@type='file']")
    SUBMIT_BUTTON = ("xpath", "//input[@data-qa='submit-button']")
    SUCCESS_MESSAGE = ("xpath", "//div[@class='status alert alert-success']")

    @allure.step("Enter name.")
    def enter_name(self, name):
        self.enter_text(self.NAME_FIELD, name)

    @allure.step("Enter email.")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Enter subject.")
    def enter_subject(self, subject):
        self.enter_text(self.SUBJECT_FIELD, subject)

    @allure.step("Enter message.")
    def enter_message(self, message):
        self.enter_text(self.MESSAGE_FIELD, message)

    @allure.step("Upload test file.")
    def upload_test_file(self):
        file_path = os.path.join(os.getcwd(), 'test_data', 'test_image.png')
        self.driver.find_element(*self.UPLOAD_FILE_FIELD).send_keys(file_path)

    @allure.step("Click Submit button.")
    def click_submit(self):
        self.click_element(self.SUBMIT_BUTTON)

    @allure.step("Approve alert.")
    def approve_alert(self):
        self.driver.switch_to.alert.accept()

    @allure.step("Verify success message.")
    def verify_success_message(self):
        message = self.wait_for_visibility(self.SUCCESS_MESSAGE)
        assert message.text == "Success! Your details have been submitted successfully.", \
            f"Unexpected success message: {message.text}"
