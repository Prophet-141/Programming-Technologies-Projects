import random
def det2(mat):
    det2 = mat[0][0]*mat[1][1] - mat[0][1] * mat[1][0]
    return det2
def det3(mat, n):
    for k in range(0, n-1):
        for i in range(k+1, n):
            if mat[k][k]!=0:
                v = mat[i][k]/mat[k][k]
            else:
                prov = 0
                for z in range(k+1,n):
                    if mat[k][z]!=0:
                        prov+=1
                        for c in range(0, n):
                            mat[c][k] += mat[c][z]
                        v = mat[i][k]/mat[k][k]
                        z = n
                if prov == 0:
                    return 0
            for j in range(0, n):
                mat[i][j] -= mat[k][j]*v
        print("Шаг " + str(k+1) + ":")
        for d in range(len(mat)):
            print(mat[d])
        print()
    det = 1
    for l in range(0, n):
        det = det * mat[l][l]
    return round(det)
print("Введите размерность матрицы")
n = int(input())
stroca = []
mat = []
print("Самостоятельный ввод(1) или случайный(2)?")
vyb = int(input())
if vyb == 1:
    for i in range(n):
        user_input = input("Введите целые числа через пробел: ")
        es = user_input.split()
        stroca = list(map(int, es))
        if len(stroca) < n:
            for z in range(len(stroca), n):
                stroca.append(0)
        mat.append(stroca)
        stroca = []
elif vyb == 2:
    for i in range(n):
        for j in range(n):
            stroca.append(random.randrange(-256, 256, 1))
        mat.append(stroca)
        stroca = []
print("Сама матрица:")
for i in mat:
    print(i)
print()
if n == 1:
    print(x[0][0])
if n == 2:
    print("det = " + str(det2(mat)))
if n > 2:
    print("det = " + str(det3(mat, n)))
