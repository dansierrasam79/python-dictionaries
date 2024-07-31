#check if all values are 12
init_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
final_list = []
for key, value in init_dict.items():
    if value == 12:
        final_list.append(1)
    else:
        final_list.append(0)

print(len(final_list), " values are 12")
