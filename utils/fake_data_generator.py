import random
from faker import Faker


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.user_name = self.fake.user_name()
        self.first_name = self.fake.first_name()
        self.email = self.fake.email()
        self.invalid_email = self.fake.first_name()
        self.password = self.fake.password(length=12)
        self.gender = random.choice(["Mr", "Mrs"])
        self.country = random.choice(["India", "United States", "Canada", "Australia", "Israel", "Singapore", "New Zealand"])
        self.day = self.fake.random_int(min=1, max=31)
        self.month = self.fake.month_name()
        self.year = self.fake.random_int(min=1900, max=2021)
        self.last_name = self.fake.last_name()
        self.address = self.fake.street_address()
        self.state = self.fake.state()
        self.city = self.fake.city()
        self.zipcode = self.fake.zipcode()
        self.mobile_number = self.fake.phone_number()
        self.comment = self.fake.paragraph()
        self.subject = self.fake.sentence()
        self.message = self.fake.paragraph()
        self.review = self.fake.paragraph()
