import os
import pytest
from pathlib import Path
from config.data import Data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.fake_data_generator import FakeDataGenerator
from pages.signup_page import SignupPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = Options()
    prefs = {"download.default_directory": str(Path(os.getcwd()) / "downloads")}
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_email(Data.EMAIL)
    login_page.enter_password(Data.PASSWORD)
    login_page.click_login()
    return driver


@pytest.fixture
def delete_account(driver):
    yield
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_delete_account()
    home_page.verify_account_deleted_message()


@pytest.fixture
def new_user_created(driver):
    fake = FakeDataGenerator()
    signup_page = SignupPage(driver)
    signup_page.open()
    signup_page.enter_user_name(fake.user_name)
    signup_page.enter_email(fake.email)
    signup_page.click_signup()
    signup_page.select_gender(fake.gender)
    signup_page.enter_password(fake.password)
    signup_page.select_day(fake.day)
    signup_page.select_month(fake.month)
    signup_page.select_year(fake.year)
    signup_page.enter_first_name(fake.first_name)
    signup_page.enter_last_name(fake.last_name)
    signup_page.enter_address(fake.address)
    signup_page.select_country(fake.country)
    signup_page.enter_state(fake.state)
    signup_page.enter_city(fake.city)
    signup_page.enter_zipcode(fake.zipcode)
    signup_page.enter_mobile_number(fake.mobile_number)
    signup_page.click_create_account()
    return fake


@pytest.fixture
def clean_downloads_directory():
    downloads_dir = Path(os.getcwd()) / "downloads"
    downloads_dir.mkdir(parents=True, exist_ok=True)
    for file in downloads_dir.iterdir():
        if file.is_file():
            file.unlink()
    return downloads_dir
