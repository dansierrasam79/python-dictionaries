#change value from str to int
init_list = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
final_list = []
for dct in init_list:
    temp_dict = {}
    for key,value in dct.items():
        temp_dict[key] = int(value)
    final_list.append(temp_dict)
print(final_list)
