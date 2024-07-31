#remove dict from list
init_list = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
temp_dict = {}
final_list = []
for dct in init_list:
    if '#FF0000' in dct.values() or 'Red' in dct.values():
        print("Delete")
    else:
        final_list.append(dct)

print(final_list)
