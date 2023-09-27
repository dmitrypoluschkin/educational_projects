import random
import time
import sys

# Задаем константы:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

# Спрашиваем, сколько улиток должно участвовать в бегах:
while True:
    print(f'Сколько улиток будет участвовать в забеге? Max: {MAX_NUM_SNAILS}')
    response = input('Введи кол-во: ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
        print(f'Введите число от 2 до {MAX_NUM_SNAILS}')

# Ввод имен всех улиток:
snailNames = []  # Список имен улиток в виде строковых значений.
for i in range(1, numSnailsRacing + 1):
    while True:
        print(f'Введите имя улитки #{i} name:')
        name = input('Введите имя: ')
        if len(name) == 0:
            print('Пожалуйста, введите имя')
        elif name in snailNames:
            print('Выберите имя, которое еще не использовалось.')
        else:
            break
    snailNames.append(name)

# Отображаем всех улиток на старте.
print('\n' * 2)
print(f'{"START":<{FINISH_LINE}}FINISH')
print(f'{"|":<{FINISH_LINE}}|')
snailProgress = {}
for snailName in snailNames:
    print(f'{snailName[:MAX_NAME_LENGTH]}')
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)  # Пауза перед началом гонок.

while True:  # Основной цикл программы.
    # Выбираем случайным образом, каких улиток двигать вперед:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

    # Проверка на завершение гонки (например, первая улитка достигла финишной линии):
    if any(progress >= FINISH_LINE for progress in snailProgress.values()):
        print("Гонка завершена!")
        break

    time.sleep(0.5)

    # Отображает стартовую и финишную прямые:
    print(f'{"START":<{FINISH_LINE}}FINISH')
    print(f'{"|":<{FINISH_LINE}}|')

    # Отображает улиток (с метками имен):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print(f'{" " * spaces}{snailName[:MAX_NAME_LENGTH]}')
        print('.' * snailProgress[snailName] + '@v')

# Выход из программы
sys.exit()





