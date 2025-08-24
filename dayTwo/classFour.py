class Name:
	data = 10 #class data 
	def methodOne(self): #instance method 
		self.dataOne = 100 #instance data 
		print(f'methodOne... {id(self)}   dataOne: {self.dataOne}')
		
	def methodTwo(self, a, b, *arg, **kwargs):
		pass


if __name__ =='__main__':

    a = Name()
    b = Name() 
    a.methodOne()
    b.methodOne()
    #print(f'Class data: {Name.data}') 
