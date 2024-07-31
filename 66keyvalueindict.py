init_list = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
key_src = 'student_id'
value_src = 2
key2_src = 'name'
value2_src = 'Lynne Foster'

for stud_dict in init_list:
    for key, value in stud_dict.items():
        if key == key2_src and value == value2_src:
            print(True)
        else:
            print(False)
