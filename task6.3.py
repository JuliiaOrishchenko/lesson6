original_list = []
final_list = []
counter = 0
counter2 = 0
while counter < 100:
    counter += 1
    original_list.append(counter)

while counter2 < 100:
    if original_list[counter2] % 7 == 0 and original_list[counter2] % 5 != 0:
        final_list.append(original_list[counter2])
    counter2 += 1
print(final_list)
