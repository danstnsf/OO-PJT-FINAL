from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from random import randint

class CoinMovement:
    def __init__(self, window, make_canvas):
        self.window = window
        self.make_canvas = make_canvas
        self.made_red_coin = [None, None]  # Substitua pelo tamanho necessário
        self.made_green_coin = [None, None]  # Substitua pelo tamanho necessário
        self.made_yellow_coin = [None, None]  # Substitua pelo tamanho necessário
        self.made_sky_blue_coin = [None, None]  # Substitua pelo tamanho necessário
        
        self.red_number_label = [None, None]  # Substitua pelo tamanho necessário
        self.green_number_label = [None, None]  # Substitua pelo tamanho necessário
        self.yellow_number_label = [None, None]  # Substitua pelo tamanho necessário
        self.sky_blue_number_label = [None, None]  # Substitua pelo tamanho necessário
        
        self.red_coin_position = [0, 0]  # Substitua pelo tamanho necessário
        self.green_coin_position = [0, 0]  # Substitua pelo tamanho necessário
        self.yellow_coin_position = [0, 0]  # Substitua pelo tamanho necessário
        self.sky_blue_coin_position = [0, 0]  # Substitua pelo tamanho necessário
        
    def red_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_red_coin[int(coin_number)-1])
        self.made_red_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3, outline="black")

        self.red_number_label[int(coin_number)-1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.red_number_label[int(coin_number)-1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_coin_position[int(coin_number)-1] = 1
        self.window.update()
        time.sleep(0.2)


    def green_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_green_coin[int(coin_number)-1])
        self.made_green_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="#00FF00", width=3)

        self.green_number_label[int(coin_number)-1].place_forget()
        green_start_label_x = 100 + (40*8) + 10
        green_start_label_y = 15 + 40 + 5
        self.green_number_label[int(coin_number)-1].place(x=green_start_label_x, y=green_start_label_y)

        self.green_coin_position[int(coin_number)-1] = 14
        self.window.update()
        time.sleep(0.2)


    def yellow_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_yellow_coin[int(coin_number)-1])
        self.made_yellow_coin[int(coin_number)-1] = self.make_canvas.create_oval(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)

        self.yellow_number_label[int(coin_number)-1].place_forget()
        yellow_start_label_x = 100 + (40 * 6)+(40*3)+(40*4) + 10
        yellow_start_label_y = 15 + (40*8) + 5
        self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.yellow_coin_position[int(coin_number) - 1] = 27
        self.window.update()
        time.sleep(0.2)


    def sky_blue_circle_start_position(self,coin_number):
        self.make_canvas.delete(self.made_sky_blue_coin[int(coin_number)-1])
        self.made_sky_blue_coin[int(coin_number)-1] = self.make_canvas.create_oval(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="#04d9ff",width=3)

        self.sky_blue_number_label[int(coin_number)-1].place_forget()
        sky_blue_start_label_x = 100+240 + 10
        sky_blue_start_label_y = 340+(40*5)-5 + 5
        self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

        self.sky_blue_coin_position[int(coin_number) - 1] = 40
        self.window.update()
        time.sleep(0.2)
        