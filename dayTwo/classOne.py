class Name:	
	def methodOne(self):
		self.data = 100
		print(f'self here is {id(self)}')
		
	def methodTwo(self, a, b, *arg, **kwargs):
		pass 

if __name__ == '__main__':
    obj = Name()		
    a = Name()

    print(f'obj id:{id(obj)}')
    obj.methodOne()
    print(f'a id:{id(a)}')
    a.methodOne()

