'''
    input('Prompt String') --> returns a str
'''

num = int(input('Enter a num: '))
res = 'Odd' if num % 2 else 'Even'
print(f'Num {num} is {res}')