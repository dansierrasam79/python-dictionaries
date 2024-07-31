#find keys based on specific value
init_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
spc_val = 20
final_list = []
for key,value in init_dict.items():
    if value == spc_val:
        final_list.append(key)
print(final_list)
