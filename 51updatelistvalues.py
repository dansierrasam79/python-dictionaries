#update list values
#{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
init_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
for key,value in init_dict.items():
    if key == 'Math':
        value.clear()
        value.append(89)
        value.append(90)
        value.append(91)
    elif key == 'Physics':
        value.clear()
        value.append(90)
        value.append(92)
        value.append(87)
print(init_dict)
