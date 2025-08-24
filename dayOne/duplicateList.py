'''
    Remove duplicates from a list
'''
lst = [10,20,30,40,20,30,40]
newLst = sorted(list(set(lst)))
newListOne = sorted(lst)
print(lst)
print(newLst)
print(newListOne)