#convert list of lists to dict
init_list = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
final_dict = {}
for item in init_list:
    key = item[0]
    value = [item[1],item[2]]
    final_dict[key] = value
print(final_dict)
