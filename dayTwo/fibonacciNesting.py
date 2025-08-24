'''

fibonacciNesting.py
'''

'''fibonacci.py'''

def printFiboSeries(numInSeries):
    def fibo(num):
        if num <= 1:
            return num
        return fibo(num-1) + fibo(num-2)

    for i in range(numInSeries):
        print(f'{i+1} --> {fibo(i)}')


printFiboSeries(10)