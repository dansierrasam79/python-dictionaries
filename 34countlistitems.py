#count list items
init_dict = {'a':1,'b':[2,3],'c':4, 'd':5, 'e':[5], 'f':6}
count = 0
for key,value in init_dict.items():
    if isinstance(value,(list)):
        count += 1
print(count)
