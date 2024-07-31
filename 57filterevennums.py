#filter even numbers
init_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
final_dict = {}
for key,value_list in init_dict.items():
    temp_list = []
    for item in value_list:
        if item % 2 == 0:
            temp_list.append(item)
    final_dict[key]=temp_list
print(final_dict)
