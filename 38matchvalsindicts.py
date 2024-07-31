#match values in dicts
init_dict = {'key1': 1, 'key2': 3, 'key3': 2}
init_dict2 = {'key1': 1, 'key2': 2}

for key,value in init_dict.items():
    for key2, value2 in init_dict2.items():
        if key == key2 and value == value2:
            both_key = key
            both_value = value
print(str(both_key), ":", str(both_value), "is present in both sets")
