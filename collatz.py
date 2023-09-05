import sys, time


print('''
    The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.
      
    It is generally thought, but so far not mathematically proven, that every starting number eventually terminates at 1.
''')

print('''
    Enter a starting number (greater than 0) or QUIT:
''')

response = input('> ')
if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:  # Если n  четное...
        n = n // 2
    else:    # В противном случае n - нечетное...
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()