mat =  []
#implement the logic to fill the matrix of 3 X 5 
multiplier = 10
for i in range(3):
    mat.append([])
    for j in range(1, 6):
        mat[i].append(j * multiplier)
    multiplier *= 10

for i in range(3):
    for j in range(5):
        print(mat[i][j], end=' ')
    print()

'''
for row in mat:
    for val in row:
        print(val, end = '  ')
    print()
'''