def funName(a = 1, b = 2 , *args, **kwargs):
	print(f'a: {a}  b: {b}  args: {args}  kwargs: {kwargs}')
	if 'name' in kwargs:
		print(f'kwargs["name"] --> {kwargs["name"]}')

    
funName(10,20, 30)
funName(10,20, 30, 40, 50, 60)
funName(10,20, 30, 40, 50, 60,name='Sachin',scores=10001,reverse=True)
funName(10,20, 30, 40, 50, 60,scores=10001,reverse=True)