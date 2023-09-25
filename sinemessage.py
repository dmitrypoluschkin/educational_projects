import math, shutil, sys, time


# Получаем размер окна терминала:
WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1 

print('(Press Ctrl-C to quit.)')
print()

print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('Ввод > ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')

step = 0.0 # step определяет, в каком месте синусоиды мы находимся.
# Синус принимает значения от -1.0 до 1.0, так что необходимо умножить на коэффициент:
multiplier = (WIDTH - len(message)) / 2
try:
    while True:
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep+1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25
except KeyboardInterrupt:
    sys.exit()
