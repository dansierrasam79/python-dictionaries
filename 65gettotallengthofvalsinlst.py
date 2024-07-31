#get total length of all dict values
init_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
total_length = 0
for key, value in init_dict.items():
    total_length += len(value)
print(total_length)
