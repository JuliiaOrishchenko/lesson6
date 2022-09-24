import random

first_list = []
second_list = []
i = 0
while i < 10:
    first_list.append(random.randint(0, 10))
    second_list.append((random.randint(0, 10)))
    i += 1

result = list(set(first_list) & set(second_list))

print(first_list)
print(second_list)
print(result)

