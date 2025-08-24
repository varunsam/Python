def funName(a = 1, b = 2 , *args):
	print(f'a: {a}  b: {b}  args: {args}')
	for i in args:
		print(f'\t\ti:{i} ') 
	
funName()
funName(100)
funName(100,200)
funName(10,20, 30)
funName(10,20, 30, 40, 50, 60)
funName(None, None)