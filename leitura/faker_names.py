from faker import Faker


faker = Faker(locale='es_AR')

Faker.seed(0)

print(faker.last_name())
print(faker.email())
print(faker.password())
print(faker.url())
print(faker.license_plate())
print(faker.phone_number())
