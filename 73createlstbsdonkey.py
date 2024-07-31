init_list = [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
final_list = []
spec_key = 'age'
for dct in init_list:
    for key,value in dct.items():
        if key == spec_key:
            final_list.append(value)
print(final_list)
