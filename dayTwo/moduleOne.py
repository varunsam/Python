'''moduleOne.py'''

def funOne():
    print(f'funOne() from {__name__} module')

def funTwo():
    print(f'funTwo() from {__name__} module')

def funThree():
    print(f'funThree() from {__name__} module')

dataOne=100
dataTwo=200

if __name__ == '__main__':#dunder
    funOne()
    funTwo()
    funThree() 