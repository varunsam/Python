def funName(a = 1, b = 2 , *args, **kwargs):
	print(f'a: {a}  b: {b}  args: {args}  kwargs: {kwargs}')
	if 'name' in kwargs:
		print(f'kwargs["name"] --> {kwargs["name"]}')
		
	return kwargs

    
res = funName(10,20, 30,A=100, B=200)

for var in res:
	print(f'var: {var}')