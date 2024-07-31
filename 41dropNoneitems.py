#drop None items
init_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
final_dict = {}
for key, value in init_dict.items():
    if value is not None:
        final_dict[key] = value
print(final_dict)
