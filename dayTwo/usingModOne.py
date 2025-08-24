'''
import moduleOne

moduleOne.funOne()
moduleOne.funTwo()
moduleOne.funThree()


import moduleOne as mo

if __name__ == '__main__':
    mo.funOne()
    mo.funTwo()
    mo.funThree()
    print(f'dataOne: {mo.dataOne}   dataTwo: {mo.dataTwo}')
'''

import sys
print(f'platform: {sys.platform}')
print(f'platform: {sys.path}')