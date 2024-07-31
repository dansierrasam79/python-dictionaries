init_list = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
final_dict = {}
for key, value in init_list.items():
    if value > 170:
        final_dict[key] = value
print(final_dict)
