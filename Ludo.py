from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint
from tkinter import Label, Button, Entry, DISABLED, SUNKEN
import tkinter as tk 
from coin_actions import CoinMovement 
from ButtonActions import LudoUIMethods 
from controles import Controles
from pawn import Pawn
from tabuleiro2 import Tabuleiro


class Ludo(Tabuleiro,Controles,Pawn):
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.coin_actions = CoinMovement(self.root, self.canvas)
        self.ButtonActions = LudoUIMethods(self.root, self.canvas)
    def __init__(self, root,six_side_block,five_side_block,four_side_block,three_side_block,two_side_block,one_side_block):
        self.window = root
        # Fazer canvas
        self.make_canvas = Canvas(self.window, bg="#4d4dff", width=800, height=630)
        self.make_canvas.pack(fill=BOTH,expand=1)

        # containers de data 
        self.made_red_coin = []
        self.made_green_coin = []
        self.made_yellow_coin = []
        self.made_sky_blue_coin = []

        self.red_number_label = []
        self.green_number_label = []
        self.yellow_number_label = []
        self.sky_blue_number_label = []

        self.block_value_predict = []
        self.total_people_play = []

        # image store
        self.block_number_side = [one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block]

        
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.sky_blue_coord_store = [-1, -1, -1, -1]

        self.red_coin_position = [0, 1, 2, 3]
        self.green_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.sky_blue_coin_position = [0, 1, 2, 3]

        for index in range(len(self.red_coin_position)):
            self.red_coin_position[index] = -1
            self.green_coin_position[index] = -1
            self.yellow_coin_position[index] = -1
            self.sky_blue_coin_position[index] = -1

        
        self.move_red_counter = 0
        self.move_green_counter = 0
        self.move_yellow_counter = 0
        self.move_sky_blue_counter = 0

        self.take_permission = 0
        self.six_with_overlap = 0

        self.red_store_active = 0
        self.sky_blue_store_active = 0
        self.yellow_store_active = 0
        self.green_store_active = 0

        self.six_counter = 0
        self.time_for = -1

        
        self.right_star = None
        self.down_star = None
        self.left_star = None
        self.up_star = None

        # inicializar funções
        self.board_set_up()

        self.instruction_btn_red()
        self.instruction_btn_sky_blue()
        self.instruction_btn_yellow()
        self.instruction_btn_green()

        self.take_initial_control()
class start():
    def __init__(self):
            window = Tk()
            window.geometry("800x630")
            window.maxsize(800,630)
            window.minsize(800,630)
            window.title("Ludo - Projeto Final OO")
            block_six_side = ImageTk.PhotoImage(Image.open('Images/6_block.png').resize((33, 33)))
            block_five_side = ImageTk.PhotoImage(Image.open("Images/5_block.png").resize((33, 33)))
            block_four_side = ImageTk.PhotoImage(Image.open("Images/4_block.png").resize((33, 33)))
            block_three_side = ImageTk.PhotoImage(Image.open("Images/3_block.png").resize((33, 33)))
            block_two_side = ImageTk.PhotoImage(Image.open("Images/2_block.png").resize((33, 33)))
            block_one_side = ImageTk.PhotoImage(Image.open("Images/1_block.png").resize((33, 33)))
            Ludo(window,block_six_side,block_five_side,block_four_side,block_three_side,block_two_side,block_one_side)
            make_canvas = Canvas(window)  
            CoinMovement(window, make_canvas)
            LudoUIMethods(window, make_canvas)
            window.mainloop()
