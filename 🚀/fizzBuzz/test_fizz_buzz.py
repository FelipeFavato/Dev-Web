from fizz_buzz import fizzbuzz


def test_fizzbuzz_should_return_list_of_numbers():
    assert fizzbuzz(2) == [1, 2]


def test_fizzbuzz_divisible_by_trhee_should_be_fizz():
    # Se A função fizzbuzz receber 3, então a ultima posição da lista retornada
    # deve ser 'Fizz' -> Olha esse jeito de chegar na ultima posição!!
    assert fizzbuzz(3)[-1] == 'Fizz'


def test_fizzbuzz_divisible_by_five_should_be_buzz():
    assert fizzbuzz(5)[-1] == 'Buzz'


def test_fizzbuzz_divisible_by_five_and_three_should_be_fizzbuzz():
    assert fizzbuzz(15)[-1] == "FizzBuzz"
