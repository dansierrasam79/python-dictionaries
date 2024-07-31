#create dict from string
import collections as col
init_string = 'w3resource'
init_list = [letter for letter in init_string]
cnt = col.Counter()
for letter in init_list:
    cnt[letter] += 1
print(cnt)
