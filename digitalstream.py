import random, shutil, sys, time


#задаем константы
MIN_STREAM_LENGHT = 6
MAX_STREAM_LENGHT = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

DENSITY = 0.02

# Получаем размер окна терминала
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print('Press Ctrl+C to quit')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        # Задаём счетчики для каждого из столбцов
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Перезапускаем поток для этого столбца:
                    columns[i] = random.randint(MIN_STREAM_LENGHT,
                                                MAX_STREAM_LENGHT)
                
            # Выводим пробел или символ 1/0:
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end=' ')
                columns[i] -= 1
            else:
                print(' ', end=' ')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()

