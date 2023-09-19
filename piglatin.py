"""Поросячья латынь, переводит сообщения на английском на поросячью латынь."""

try:
    import pyperclip  # pyperclip копирует текст в буфер обмена.
except ImportError:
    print("Библиотека pyperclip не установлена. Установите ее, чтобы использовать копирование в буфер обмена.")

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    user_input = input('> ')
    pigLatin = englishToPigLatin(user_input)

    # Объединяем все слова обратно в одно строковое значение:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass


def englishToPigLatin(message):
    pigLatin = ''  # Строковое значение с переводом на поросячью латынь.
    for word in message.split():
        # Отделяем небуквенные символы в начале слова:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin += prefixNonLetters + ' '
            continue

        # Отделяем небуквенные символы в конце слова:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]
        # Запоминаем, находится ли слово полностью или только первые буквы в верхнем регистре.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()  # Переводим слово в нижний регистр для перевода.

        # Отделяем согласные буквы в начале слова:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # Добавляем в слово "поросячье" окончание:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'

        # Переводим слово полностью или только первые буквы обратно в верхний регистр:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # Добавляем небуквенные символы обратно в начало слова.
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '

    return pigLatin


if __name__ == '__main__':
    main()