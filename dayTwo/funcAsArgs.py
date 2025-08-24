'''
    Passsing function as argument
'''

def funCaller(func, *args):
    print('Before Function call')
    func(*args)
    print('After Function call')
    print('*' * 40)

def fun():
    print('fun() called')

def funOne(num):
    print(f'funOne({num}) called')

funCaller(fun)
funCaller(funOne, (10,20,30,40))
