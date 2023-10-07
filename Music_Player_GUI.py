# Импорт библиотек необходимых для создания приложения
import pygame # для работы с аудио
import tkinter as tkr # для графического интерфейса
from tkinter.filedialog import askdirectory # для запроса у пользователя директории с музыкальными файлами.
import os # используется для работы с операционной системой

'''Создание главного окна приложения'''
music_player = tkr.Tk() # Создает главное окно приложения.
music_player.title("My Music Player")# Устанавливает заголовок окна.
music_player.geometry("450x350")# Устанавливает размер окна.

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
pos = 0  # Переменная pos инициализируется здесь
for item in song_list:
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)  # Исправлено на tkr.Label

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")
music_player.mainloop()

            
