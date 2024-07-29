# concatenate dictionaries
init_dict={1:10, 2:20}
init_dict2={3:30, 4:40}
init_dict3={5:50,6:60}
final_dict = {}
for k,v in init_dict.items():
    final_dict[k] = v

for k,v in init_dict2.items():
    final_dict[k] = v

for k,v in init_dict3.items():
    final_dict[k] = v

print(final_dict)
