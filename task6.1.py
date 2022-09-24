from random import randint

final_list = []
i = 0

while i < 10:
    final_list.append(randint(0, 100))
    i += 1

print(final_list)
print(max(final_list))
