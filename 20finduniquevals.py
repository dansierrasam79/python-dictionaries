#Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
init_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
final_list_keys = []
final_list_values = []
for ind_dict in init_list:
    for k,v in ind_dict.items():
        if v not in final_list_values:
            final_list_values.append(v)
print(set(final_list_values))
