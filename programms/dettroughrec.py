import sys
sys.setrecursionlimit(2000000000)
def detn (mat):
    if (len(mat) == 1):
        return mat[0][0]
    n = len(mat)
    de = 0
    for i in range(n):
        M_table = []
        for j in range(1, n):
            M_string = []
            for k in range(n):
                if k != i:
                    M_string.append(mat[j][k])
            M_table.append(M_string)
        M = detn(M_table)
        de += mat[0][i] * (-1)**(0+i) * M
    return de


n = int(input())
Massiv = []
for i in range(n):
    Massiv.append(list(map(int, input().split())))
print('det(Massiv) = ', detn(Massiv))
