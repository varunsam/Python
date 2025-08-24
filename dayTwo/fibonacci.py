'''
    fibonacci.py
'''

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

def printFiboSeries(num):
    for i in range(num):
        print(f'{i+1} --> {fibo(i)}')

printFiboSeries(10)