def test_faker_email(faker):
    fake_email = faker.email()
    assert isinstance(fake_email, str)
    assert '@' in fake_email
    assert '.' in fake_email
