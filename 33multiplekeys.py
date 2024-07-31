# do multiple keys exist
#init_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
init_dict = {'a':1}
final_list = list(init_dict.keys())
if len(final_list) > 1:
    print("Multiple keys exist")
else:
    print("Single key")
