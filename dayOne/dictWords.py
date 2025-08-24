strings = '''
        Returns value or default
        Returns view of keys
        Returns view of values
        Returns key value  pairs
        Updates with another dict
        Removes key returns value
        Removes and returns last key value
        Removes all items
        Shallow copy 
        Returns value if key exists, else
    '''
dt = {}
for word in strings.split():
    key = word.lower()
    if key not in dt:
        dt.setdefault(key, 1)
    else:
        dt[key] += 1

print(dt)

for k,v in dt.items():#dt.values(): #dt.keys()
    print(f'key: {k}  --> {v}')