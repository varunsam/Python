'''
'''
num = int(input('Enter a num: '))
lastDigit, lastTwoDigits = num % 10 , num % 100

if lastDigit == 1 and lastTwoDigits != 11:
    print(f'{num}st')
elif lastDigit == 2 and lastTwoDigits != 12:
    print(f'{num}nd')
elif lastDigit == 3 and lastTwoDigits != 13:
    print(f'{num}rd')
else:
    print(f'{num}th')