from faker import Faker

fake = Faker()

class BaseGenerator:
    fullname = f"{fake.first_name()}{fake.last_name()}"
    username = f"{fake.word()}{fake.random_int(0, 999999)}"
    password = fake.password()
    confirm_password = fake.password()
    email = fake.email()
    random_int = fake.random_int(0, 999999)