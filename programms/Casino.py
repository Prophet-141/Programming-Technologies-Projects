import random

while True:

    print('___________________________________')
    stavka = float(input('Кошелек: $'))
    print('Играем? (Играем // Не играем) ;)')

    while input().capitalize().strip() == 'Играем' and stavka != 0:
        print('Сделайте денежную ставку(в %: на число, на цвет, на четность): ')
        C = list(map(int, input().split()))
        if (C[0]+C[1]+C[2] > 100 or C[0] < 0 or C[1] < 0 or C[2] < 0):
            print('!!!Ошибка!!! Пожалуйста, введите коректные процентные числа')
            print('Играем? (Играем // Не играем) ;)')
            continue
        C = [round(C[0] / 100 * stavka, 2), round(C[1] / 100 * stavka, 2), round(C[2] / 100 * stavka, 2)]
        stavka -= (C[0] + C[1] + C[2])
        print(*C)

        print('Сделайте ставку(число, цвет, четность): ')
        B = list(map(str, input().split()))
        B[0] = int(B[0])
        B[1] = B[1].capitalize()
        B[2] = B[2].capitalize()

        A = []
        A.append(random.randint(0, 36))

        if A[0] in [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]:
            A.append('Красное')
        elif A[0] == 0:
            A.append('Зеленое')
        else:
            A.append('Черное')

        if A[0] % 2 == 0:
            A.append('Четное')
        else:
            A.append('Нечетное')

        print('Результат: ', *A)

        if A[0] == B[0]:
            C[0] *= 3
        else:
            C[0] = 0
        if B[1] == A[1]:
            C[1] *= 2
        else:
            C[1] = 0
        if A[2] == B[2]:
            C[2] *= 2
        else:
            C[2] = 0
        print('___________________________________')

        stavka = round(stavka + C[0] + C[1] + C[2], 2)
        print('Кошелек: $', stavka, sep='')

        print('Играем? (Играем // Не играем) ;)')

    print()
    print()
    print()
    print('                  ВИДИМО, ВЫ ВСЁ ПРОИГРАЛИ :(')
    print('         ПОЖАЛУйСТА, ПОПОЛНИТЕ СЧЕТ, ЧТОБЫ ИГРАТЬ ДАЛЬШЕ')





