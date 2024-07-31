#extract list of values
init_list = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
final_list = []
for item in init_list:
    for key, value in item.items():
        if key == 'Math':
            final_list.append(value)
print(final_list)
