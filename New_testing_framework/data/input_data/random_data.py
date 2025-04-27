import random
import string
import faker
from faker import Faker


class RandomData:
    fake = Faker()


def random_string(n):
    return ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase, k=n))


def random_string_lowercase(n):
    return ''.join(random.sample(string.ascii_lowercase, k=n))


def random_numbers():
    return faker.generator.random.randint(1, 9)

def generate_random_float() -> float:
    return round(random.uniform(0, 5), 2)

def random_numbers_choose_number():
    return faker.generator.random.randint(80, 396)


def random_numbers_bills():
    return faker.generator.random.randint(1, 101)
