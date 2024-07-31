# filter weight and height of students
init_dict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
final_dict = {}
for key,value in init_dict.items():
    if value[0] >= 6 and value[1] >= 70:
        final_dict[key] = value
print(final_dict)
    
