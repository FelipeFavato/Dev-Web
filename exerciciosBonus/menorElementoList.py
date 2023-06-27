numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]


def find_smallest_int(numbers: list) -> int:
    smallest_number = numbers[0]
    for value in numbers:
        if value < smallest_number:
            smallest_number = value
    return smallest_number


print(find_smallest_int(numbers))


def minimum(numbers):
    return min(numbers)


# ou mesmo
# minimum = min
