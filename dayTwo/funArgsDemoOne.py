'''funArgsDemoOne.py'''


'''
funArgsDemo.py
    Passsing function as argument
'''
import time 
def funCaller(func, *args):
    start = time.time()
    if len(args) >= 1:
        res = func(args[0])
    else:
        res = func(5)

    end = time.time()
    print(f'Time taken: {round(end-start, 3)} res: {res}')
    print('*' * 40)

funCaller(lambda x: x + 2, 10)
funCaller(lambda x: x + 2)
funCaller(lambda x: x ** 2, 10)
funCaller(lambda x: x ** 2, 100)
