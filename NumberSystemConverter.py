# Изначальные данные и константы.
SYMBOLS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYSTEMS = '₀₁₂₃₄₅₆₇₈₉'
digits = []
answer = ''
summ = 0
not_bigger_than_system_base = True
correct_format = True
non_existing_system_base = False

# Функция для создания маленьких чисел системы счисления.
def system_modifier(system):
    if len(str(system)) == 1:
        system = SYSTEMS[system]
    else:
        digit1 = int(system / 10)
        digit2 = int(system % 10)
        digit1 = SYSTEMS[digit1]
        digit2 = SYSTEMS[digit2]
        system = str(digit1) + str(digit2)
    return system

if osnovan == drugoe:
    g = False

# Вводные данные
num = str(input('Введите число: '))
initial_system_base = str(input('Введите систему счисления числа: '))
transfer_to_system_base = str(input('Введите систему счисления, в которую нужно перевести: '))

# Проверка на корректность системы счисления.
if (not(initial_system_base.isdigit())) or (not(transfer_to_system_base.isdigit())):
    non_existing_system_base = True
else:
    initial_system_base = int(initial_system_base)
    transfer_to_system_base = int(transfer_to_system_base)
    if (initial_system_base < 2) or (transfer_to_system_base < 2):
        non_existing_system_base = True

# Проверка формата числа (нет ли некорректных символов).
for letter in num:
    if letter.upper() not in SYMBOLS:
        correct_format = False
        break

if g == False:
    print('Основания должны отличаться друг от друга.')

if f == False:
    print(osnovan,'система счисления начинается от 0 и заканчивается',osnovan-1,'. Введите число заново.')

if n == False:
    print('Неправильный формат. Если вы пишите букву, то она должа быть Английской, а не Русской. Введите число заново. ')

if (f == True) and (g == True) and (n == True):
    if osnovan == 10 and drugoe >= 2 and drugoe != 10:
        while int(a) > 0:
            shest = int(a) % drugoe
            a = int(a) // drugoe
            if drugoe > 10:
                if shest == 10:
                    shest = 'A'
                if shest == 11:
                    shest = 'B'
                if shest == 12:
                    shest = 'C'
                if shest == 13:
                    shest = 'D'
                if shest == 14:
                    shest = 'E'
                if shest == 15:
                    shest = 'F'
                otvet = str(shest) + otvet
            else:
                otvet = str(shest) + otvet
        print(otvet,'(',drugoe,')') #Десятеричная система счисления в шестнадцатеричной системе счисления

    elif drugoe == 10 and osnovan >= 2 and osnovan != 10:
        c.reverse()
        for i in range(len(c)):
            perevod1 = int(c[i])*(osnovan**i)
            summ = perevod1+summ
        print(summ,'(',drugoe,')') #Пятеричная система счисления в десятичной системе счисления

    else:
        c.reverse()
        for i in range(len(c)):
            perevod1 = int(c[i]) * (osnovan ** i)
            summ = perevod1 + summ

        while summ > 0:
            shest = summ % drugoe
            summ = summ // drugoe
            if drugoe > 10:
                if shest == 10:
                    shest = 'A'
                if shest == 11:
                    shest = 'B'
                if shest == 12:
                    shest = 'C'
                if shest == 13:
                    shest = 'D'
                if shest == 14:
                    shest = 'E'
                if shest == 15:
                    shest = 'F'
                otvet = str(shest) + otvet
            else:
                otvet = str(shest) + otvet

        print(otvet,'(',drugoe,')') #Десятеричная система счисления в шестнадцатеричной системе счисления

