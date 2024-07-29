#gen dict in the k:v form of x:x*x
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
init_dict = {x:x*x for x in range(0,5)}
print(init_dict)
