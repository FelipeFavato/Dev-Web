def biggest(first: int, second: int) -> int:
    if first > second:
        return first
    return second


print(biggest(10, 2))
print(biggest(10, 15))
print(biggest(10, 10))
