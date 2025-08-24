'''
    lambdaOne.py
        Intro to lambda expressions
'''

#

exprOne = lambda x: x * x
exprTwo = lambda x,y: x ** y

print(f'ExprOne: {exprOne(10)}')
print(f'ExprTwo: {exprTwo(2,10)}')

lst = [10,20,30,40,50,60]
res = list(map(lambda x: x+2, lst))
print(res)

def funTest(x):
    return x + 2

res = list(map(funTest, lst))
print(res)




