#max values in dictionary
init_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
init_list = []
final_dict = {}
max_values = 3
for key, value in init_dict.items():
    init_list.append(value)
init_list.sort(reverse=True)

for item in init_list[:3]:
    for key, value in init_dict.items():
        if value == item:
            final_dict[key] = value
print(final_dict)
