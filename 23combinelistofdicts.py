#combinevalsinlstofdicts
init_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
final_list = []
final_dict = {}
for init_dict in init_list:
    temp_list = []
    for k,v in init_dict.items():
        temp_list.append(v)
    final_list.append(temp_list)

for lst in final_list:
    total = 0
    for lst2 in final_list:
        if lst[0] == lst2[0]:
            total += lst2[1]
    if lst[0] not in final_dict.keys():
        final_dict[lst[0]] = total    
print(final_dict)
