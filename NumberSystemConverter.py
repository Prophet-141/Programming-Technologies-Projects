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

# Замена букв в числе на цифры (если буквы есть) и запись в массив + проверка на непревышение системы счисления.
if (correct_format == True) and (non_existing_system_base == False):
    for i in num:
        i = SYMBOLS.index(i.upper())
        if int(i) <= initial_system_base - 1:
            digits.append(str(i))
        else:
            not_bigger_than_system_base = False
            break

# Проверка, чтобы цифры в числе не превышали значение системы счисления числа (Отрицательный результат).
if not_bigger_than_system_base == False:
    print(f'Число {num} не соответствует системе счисления {initial_system_base}. Пожалуйста, введите число заново.')

# Проверка, чтобы число не содержало некорректных символов (Отрицательный результат).
if (correct_format == False):
    print(f'Неправильный формат. В числе {num} присутствует некорректый символ. Пожалуйста, введите число заново. ')

# Проверка на корректность системы счисления (Отрицательный результат).
if non_existing_system_base == True:
    if isinstance(initial_system_base, int):
        if initial_system_base < 2:
            print(f'Исходной системы счисления, равной {initial_system_base}, не существует. '
                  f'Пожалуйста, введите систему счисления заново.')
    if isinstance(transfer_to_system_base, int):
        if transfer_to_system_base < 2:
            print(f'Системы счисления {transfer_to_system_base}, в которую нужно перевести, не существует. '
                  f'Пожалуйста, введите систему счисления заново.')
    elif not(initial_system_base.isdigit()) or not(transfer_to_system_base.isdigit()):
        print('Введённые системы счисления содержат недопустимые символы или их не существует.')

if (not_bigger_than_system_base == True) and (correct_format == True) and (non_existing_system_base == False):
    # Перевод, когда исходная система счисления и та, в которую нужно перевести, равны.
    if (initial_system_base == transfer_to_system_base) and (transfer_to_system_base >= 2) and (initial_system_base >= 2):
        print(f'{num}{system_modifier(transfer_to_system_base)}')
        
    # Перевод из 10-тичной системы счисления в любую другую систему счисления.
    elif initial_system_base == 10 and transfer_to_system_base >= 2 and transfer_to_system_base != 10:
        if int(num) != 0:
            while int(num) > 0:
                ost = int(num) % transfer_to_system_base
                ost = SYMBOLS[ost]
                answer = str(ost) + answer
                num = int(num) // transfer_to_system_base
            print(f'{answer}{system_modifier(transfer_to_system_base)}')
        else:
            print(f'0{system_modifier(transfer_to_system_base)}')

    # Перевод из любой системы счисления в 10-тичную систему счисления.
    elif (transfer_to_system_base == 10) and (initial_system_base >= 2) and (initial_system_base != 10):
        digits.reverse()
        for i in range(len(digits)):
            perevod1 = int(digits[i]) * (initial_system_base ** i)
            summ = perevod1 + summ
        print(f'{summ}{system_modifier(transfer_to_system_base)}')

    # Перевод из любой системы счисления в другую любую систему счисления.
    else:
        if summ != 0:
            digits.reverse()
            for i in range(len(digits)):
                perevod1 = int(digits[i]) * (initial_system_base ** i)
                summ = perevod1 + summ
            while summ > 0:
                ost = summ % transfer_to_system_base
                ost = SYMBOLS[ost]
                answer = str(ost) + answer
                summ = summ // transfer_to_system_base
            print(f'{answer}{system_modifier(transfer_to_system_base)}')
        else:
            print(f'0{system_modifier(transfer_to_system_base)}')

