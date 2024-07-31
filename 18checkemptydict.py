#check empty dict

init_list = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6},{}]
for item in init_list:
    print(len(item) == 0)

