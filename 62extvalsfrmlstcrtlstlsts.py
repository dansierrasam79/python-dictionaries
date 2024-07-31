#extract vals and create lst of lsts
init_list = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
 {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
final_list = []
for item in init_list:
    temp_list = []
    for key,value in item.items():
        temp_list.append(value)
    final_list.append(temp_list)
print(final_list)
