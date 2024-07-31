#split into list of dicts
init_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
final_list = []
subjects = list(init_dict.keys())
marks = list(init_dict.values())
for i in range(0, len(marks[0])):
    final_dict = {}
    final_dict[subjects[0]] = marks[0][i]
    final_dict[subjects[1]] = marks[1][i]
    final_list.append(final_dict)
print(final_list)
