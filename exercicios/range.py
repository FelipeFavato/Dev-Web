word = 'Felipe'
print(range(len(word)))

for removed_letters in range(len(word)):
    for index in range(len(word) - removed_letters):
        print(word[index], end="")
    print()


example_1 = range(5)
example_2 = range(5, 100)
example_3 = range(5, 100, 2)

# print(example_1)
# for number in example_1:
#     print(number)


# print(example_2)
# for number in example_2:
#     print(number)


# print(example_3)
# for number in example_3:
#     print(number)
