import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.contact_us_page import ContactUsPage
from pages.brand_products_page import BrandProductsPage
from pages.products_category_page import ProductsCategoryPage
from config.data import Data



class BaseTest:

    data: Data
    login_page: LoginPage
    home_page: HomePage
    signup_page: SignupPage
    account_created_page: AccountCreatedPage
    products_page: ProductsPage
    product_details_page: ProductDetailsPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    payment_page: PaymentPage
    contact_us_page: ContactUsPage
    brand_products_page: BrandProductsPage
    products_category_page: ProductsCategoryPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.signup_page = SignupPage(driver)
        request.cls.account_created_page = AccountCreatedPage(driver)
        request.cls.products_page = ProductsPage(driver)
        request.cls.product_details_page = ProductDetailsPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.payment_page = PaymentPage(driver)
        request.cls.contact_us_page = ContactUsPage(driver)
        request.cls.brand_products_page = BrandProductsPage(driver)
        request.cls.products_category_page = ProductsCategoryPage(driver)


