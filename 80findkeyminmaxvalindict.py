#find key of min max val in dict
init_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
vals_lst = []
vals_lst= list(init_dict.values())
final_list = []

for key,value in init_dict.items():
    if value == max(vals_lst):
        final_list.append(key)
    if value == min(vals_lst):
        final_list.append(key)
print(final_list)
