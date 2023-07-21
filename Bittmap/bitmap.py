
import sys


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print ('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Проходим циклом по всем строкам в битовой карте.
for line in bitmap.splitlines():
    # проходим в цикле по всмем символам в строке.
    for i, bit in enumerate(line):
        if bit == ' ':
            # выводим пустое пространство согласно пробелу в битовой строке.
            print(' ', end='')

        else:
            # выводим символ сообщения.
            print(message[i % len(message)], end='')

    print() # выводим символ новой строки
