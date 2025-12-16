from faker import Faker
from data.dataclasses.create_user_dataclass import CreateUserDataClass

fake = Faker()

class CreateUserGenerator:

    def create_user_generator(self):
        yield CreateUserDataClass(
            username=fake.user_name(),
            password=fake.password(),
            fullname=fake.last_name(),
            email=fake.email()
        )