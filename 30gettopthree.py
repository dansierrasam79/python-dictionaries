#get top three items in store
init_list = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
final_list = []
final_dict = {}
for key, value in init_list.items():
    final_list.append(value)
final_list.sort(reverse = True)

for item in final_list[:3]:
    for key, value in init_list.items():
        if value == item:
            final_dict[key] = value
print(final_dict)
