import random
def det2(mat):
    det2 = mat[0][0]*mat[1][1] - mat[0][1] * mat[1][0]
    return det2
def det3(mat, n):
    shag = 0
    for k in range(0, n-1):
        for i in range(k+1, n):
            if mat[k][k]!=0:
                v = mat[i][k]/mat[k][k]
            else:
                prov = 0
                for z in range(k+1,n):
                    if mat[k][z]!=0:
                        prov+=1
                        butter = z + 1
                        for c in range(0, n):
                            mat[c][k] += mat[c][z]
                        v = mat[i][k]/mat[k][k]
                        z = n
                if prov != 0:
                    shag += 1
                    print("Шаг " + str(shag) + ":")
                    print("Прибавим к столбику " + str(k+1) + " столбик " + str(butter))
                    for d in range(len(mat)):
                        print(mat[d])
                if prov == 0:
                    return 0
            for j in range(0, n):
                mat[i][j] -= mat[k][j]*v
            if v != 0 and v != 1:
                shag+=1
                print("Шаг " + str(shag) + ":")
                print("Вычтем из строки " + str(i+1) + " строку " + str(k+1) + " умноженную на " + str(v))
                for d in range(len(mat)):
                    print(mat[d])
            if v == 1:
                shag+=1
                print("Шаг " + str(shag) + ":")
                print("Вычтем из строки " + str(i+1) + " строку " + str(k+1))
                for d in range(len(mat)):
                    print(mat[d])
            print()
    det = 1
    for l in range(0, n):
        det = det * mat[l][l]
    return round(det)
q = 0
while q == 0:
    try:
        print("Введите размерность матрицы")
        n = int(input())
    except ValueError:
        print("Ошибка нецелочисленное значение")
    else:
        q = 1
q = 0
stroca = []
mat = []
print("Самостоятельный ввод(1) или случайный(2)?")
vyb = 0
while vyb != 1 and vyb != 2:
    vyb = int(input())
    if vyb == 1:
        for i in range(n):
            q = 0
            while q == 0:
                try:
                    user_input = input("Строка " + str(i+1) + " введите целые числа через пробел: ")
                    es = user_input.split()
                    stroca = list(map(int, es))
                except ValueError:
                    print("Ошибка нецелочисленное значение")
                else:
                    q = 1
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
print()
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
