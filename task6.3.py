original_list = list(range(1, 101))
final_list = []
index = 0

while original_list[index] < 100:
    if original_list[index] % 7 == 0 and original_list[index] % 5 != 0:
        final_list.append(original_list[index])
    index += 1
print(final_list)
