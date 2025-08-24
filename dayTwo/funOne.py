def funName(a, b, *args):
	print(f'a: {a}  b: {b}  args: {args}') 
	
funName(10,20, 30)
funName(10,20, 30, 40, 50, 60)
funName(10,20)
funName('A','Some', 30)

funName(('A','Some', 30), 200, 300)