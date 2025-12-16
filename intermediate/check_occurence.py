
"""
note we can do count for list 

which mean we can do string_list.count(character)

and to update string 

for i in stringlist:
    store[i] = store.get(i,0) + 1
"""
def check_occurence_string(string_list: list):
    store = {}
    length = len(string_list)
    for i in range(length):
        if string_list[i] not in store:
            store.update({string_list[i]:1})
        else:
            store[string_list[i]]= store[string_list[i]] + 1

    return store


from collections import Counter
print(Counter("hello"))

print(check_occurence_string("hello"))
        
