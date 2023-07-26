"""
    Взлом шифра Цезаря. Данная программа взламывает сообщения, зашифрованные шифром Цезаря, 
    путем прямого перебора всех возможных ключей.
"""

# Просим пользователя ввести сообщение для взлома:
print('Enter Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Все возможные символы для шифрования/дешифровки:
# (должно совпадать с набором SYMBOLS, использовавшимся при шифровании)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Проходим в цикле по всем возможным ключам.
    translated = ''

    # Расшифровываем каждый символ в сообщении:
    for symbol in message:
        if symbol in SYMBOLSON:
            num = SYMBOLSON.find(symbol) # Получаем числовое значение символа.
            num = num - key # Расшифровываем числовое значение.

            # Выполняем переход по кругу, если число меньше 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Добавляем соответствующий числу расшифрованный символ в translated:
            translated = translated + SYMBOLS[num]
        else:
            # Просто добавляем символ без расшифровки:
            translated = translated + SYMBOLS

# Выводим проверяемый ключ вместе с расшифрованным на его основе текстом:
print(f'Key #{key}: {translated}')
