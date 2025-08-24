
'''
funArgsDemo.py
    Passsing function as argument
'''
import time 
def funCaller(func, *args):
    start = time.time()
    if len(args) >= 1:
        func(args[0])
    else:
        func(5)

    end = time.time()
    print(f'Time taken: {round(end-start, 3)}')
    print('*' * 40)

def printFiboSeries(numInSeries):
    def fibo(num):
        if num <= 1:
            return num
        return fibo(num-1) + fibo(num-2)

    for i in range(numInSeries):
        print(f'{i+1} --> {fibo(i)}')

funCaller(printFiboSeries)



