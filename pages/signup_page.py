import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support.select import Select


class SignupPage(BasePage):

    PAGE_URL = Links.SIGNUP_PAGE

    USER_NAME_FIELD = ("xpath", "//input[@data-qa='signup-name']")
    EMAIL_FIELD = ("xpath", "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = ("xpath", "//button[@data-qa='signup-button']")
    MR_RADIO_BUTTON = ("xpath", "//label[@for='id_gender1']")
    MRS_RADIO_BUTTON = ("xpath", "//label[@for='id_gender2']")
    PASSWORD_FIELD = ("xpath", "//input[@data-qa='password']")
    DAY_SELECT = ("xpath", "//select[@data-qa='days']")
    MONTH_SELECT = ("xpath", "//select[@data-qa='months']")
    YEAR_SELECT = ("xpath", "//select[@data-qa='years']")
    FIRST_NAME_FIELD = ("xpath", "//input[@data-qa='first_name']")
    LAST_NAME_FIELD = ("xpath", "//input[@data-qa='last_name']")
    ADDRESS_FIELD = ("xpath", "//input[@data-qa='address']")
    COUNTRY_SELECT = ("xpath", "//select[@data-qa='country']")
    STATE_FIELD = ("xpath", "//input[@data-qa='state']")
    CITY_FIELD = ("xpath", "//input[@data-qa='city']")
    ZIPCODE_FIELD = ("xpath", "//input[@data-qa='zipcode']")
    MOBILE_NUMBER_FIELD = ("xpath", "//input[@data-qa='mobile_number']")
    CREATE_ACCOUNT_BUTTON = ("xpath", "//button[@data-qa='create-account']")
    ERROR_MESSAGE = ("xpath", "//p[@style='color: red;']")

    @allure.step("Enter user name.")
    def enter_user_name(self, user_name):
        self.enter_text(self.USER_NAME_FIELD, user_name)

    @allure.step("Enter email.")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Click Signup button.")
    def click_signup(self):
        self.click_element(self.SIGNUP_BUTTON)

    @allure.step("Select gender.")
    def select_gender(self, gender):
        if gender == "Mr":
            self.click_element(self.MR_RADIO_BUTTON)
        elif gender == "Mrs":
            self.click_element(self.MRS_RADIO_BUTTON)

    @allure.step("Enter password.")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("Select day.")
    def select_day(self, day):
        DAY_DROPDOWN = Select(self.driver.find_element(*self.DAY_SELECT))
        DAY_DROPDOWN.select_by_visible_text(str(day))

    @allure.step("Select month.")
    def select_month(self, month):
        MONTH_DROPDOWN = Select(self.driver.find_element(*self.MONTH_SELECT))
        MONTH_DROPDOWN.select_by_visible_text(month)

    @allure.step("Select year.")
    def select_year(self, year):
        YEAR_DROPDOWN = Select(self.driver.find_element(*self.YEAR_SELECT))
        YEAR_DROPDOWN.select_by_visible_text(str(year))

    @allure.step("Enter first name.")
    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Enter last name.")
    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_FIELD, last_name)

    @allure.step("Enter address.")
    def enter_address(self, address):
        self.enter_text(self.ADDRESS_FIELD, address)

    @allure.step("Select country.")
    def select_country(self, country):
        COUNTRY_DROPDOWN = Select(self.driver.find_element(*self.COUNTRY_SELECT))
        COUNTRY_DROPDOWN.select_by_visible_text(country)

    @allure.step("Enter state.")
    def enter_state(self, state):
        self.enter_text(self.STATE_FIELD, state)

    @allure.step("Enter city.")
    def enter_city(self, city):
        self.enter_text(self.CITY_FIELD, city)

    @allure.step("Enter zipcode.")
    def enter_zipcode(self, zipcode):
        self.enter_text(self.ZIPCODE_FIELD, zipcode)

    @allure.step("Enter mobile number.")
    def enter_mobile_number(self, mobile_number):
        self.enter_text(self.MOBILE_NUMBER_FIELD, mobile_number)

    @allure.step("Click Create account button.")
    def click_create_account(self):
        element = self.wait_for_visibility(self.CREATE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Verify signup error message.")
    def verify_error_message(self):
        error_message = self.wait_for_visibility(self.ERROR_MESSAGE)
        assert error_message.text == "Email Address already exist!", \
            f"Expected error message: Email Address already exist! But got: '{error_message.text}'."

    @allure.step("Verify email field validation is triggered.")
    def verify_email_validation(self):
        message = self.get_validation_message(self.EMAIL_FIELD)
        assert message, \
            "Expected browser validation message for the email field, but the message was empty."

    @allure.step("Verify name field validation is triggered.")
    def verify_name_validation(self):
        message = self.get_validation_message(self.USER_NAME_FIELD)
        assert message, \
            "Expected browser validation message for the name field, but the message was empty."
