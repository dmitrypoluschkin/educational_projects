'''
Чтобы создать игру в камень, ножницы, бумагу с помощью Python, нам нужно
воспользоваться выбором пользователя, а затем сравнить его с выбором компьютера,
который делается с помощью модуля random в Python из списка вариантов, и если
пользователь выиграет, то счет увеличится на 1
'''

import random

choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)  # Обновляем выбор компьютера на каждой итерации
    player = input("Choose, rock, scissors or paper and enter your answer:").capitalize()
    
    if player == computer:
        print('Tie')
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    elif player == "End":
        print("Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break