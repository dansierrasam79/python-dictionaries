#convert dict to list of lists
init_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
final_list = []
for key, value in init_dict.items():
    temp_list = []
    temp_list.append(key)
    temp_list.append(value)
    final_list.append(temp_list)
print(final_list)
