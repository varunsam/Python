from random import randint

lst10Values = [randint(1, 100) for _ in range(10)]
print(lst10Values)

#print(f'sum: {sum(lst10Values)} len: {len(lst10Values)}')
lst10Values.sort(reverse=True)
print(lst10Values)

'''
val = lst10Values.pop()
print(f'popped: {val}')
'''