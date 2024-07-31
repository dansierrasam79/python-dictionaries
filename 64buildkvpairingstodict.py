#create k-v pairing to dict
init_dict = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
final_dict = {}
for key,value_lst in init_dict.items():
    final_dict[key] = value_lst[0]
print(final_dict)
