double = {i: i*2 for i in range(3, 21)}

print(double)


count_chars = {}

for char in string:
    if char not in count_chars:
    		count_chars[char] = 1
		count_chars[char] += 1

print(count_chars)
