#clear lists in dict
init_dict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
final_dict = {}
for key, value in init_dict.items():
    value.clear()
    final_dict[key] = value
print(final_dict)
