from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint
from tkinter import Label, Button, Entry, DISABLED, SUNKEN

class LudoUIMethods:
    def __init__(self):
        # Variáveis para armazenar posições das moedas de diferentes cores
        self.red_coin_position = [-1, -1, -1, -1]
        self.green_coin_position = [-1, -1, -1, -1]
        self.yellow_coin_position = [-1, -1, -1, -1]
        self.sky_blue_coin_position = [-1, -1, -1, -1]

        # Outras variáveis necessárias
        self.block_number_side = []  # Lista para armazenar imagens dos números
        self.block_value_predict = []  # Lista para armazenar valores dos blocos
        self.six_counter = 0  # Contador para o valor 6
        self.six_with_overlap = 0  # Verificação para o valor 6 com sobreposição
        self.time_for = 0  # Contador de tempo

        # Listas para armazenar coordenadas de diferentes cores
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.sky_blue_coord_store = [-1, -1, -1, -1]

        # Janela principal
        self.window = None
        self.make_canvas = None

# Lógica para o botão vermelho
    def instruction_btn_red(self):
        block_predict_red = Label(self.make_canvas,image=self.block_number_side[0])
        block_predict_red.place(x=45,y=15)
        predict_red = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Predict", font=("Arial", 8, "bold"), command=lambda: self.make_prediction("red"))
        predict_red.place(x=37, y=15 + 40)
        entry_take_red = Entry(self.make_canvas,bg="white",fg="blue",font=("Arial",25,"bold","italic"),width=2,relief=SUNKEN,bd=5)
        entry_take_red.place(x=40,y=15+80)
        final_move = Button(self.make_canvas,bg="black",fg="#00FF00",relief=RAISED,bd=5,text="Give",font=("Arial",8,"bold"),command=lambda: self.main_controller("red",entry_take_red.get()),state=DISABLED)
        final_move.place(x=42,y=15+140)
        Label(self.make_canvas,text="Player 1",bg="#4d4dff",fg="gold",font=("Arial",15,"bold")).place(x=15,y=15+140+40)
        self.store_instructional_btn(block_predict_red,predict_red,entry_take_red,final_move)

# Lógica para o botão azul 
    def instruction_btn_sky_blue(self):
        block_predict_sky_blue = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_sky_blue.place(x=45, y=15+(40*6+40*3)+10)
        predict_sky_blue = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Predict",font=("Arial", 8, "bold"), command=lambda: self.make_prediction("sky_blue"))
        predict_sky_blue.place(x=37, y=15+(40*6+40*3)+40 + 10)
        entry_take_sky_blue = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2,relief=SUNKEN, bd=5)
        entry_take_sky_blue.place(x=40, y=15+(40*6+40*3)+40 + 50)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Give", font=("Arial", 8, "bold"),command=lambda: self.main_controller("sky_blue",entry_take_sky_blue.get()),state=DISABLED)
        final_move.place(x=42, y=15+(40*6+40*3)+40 + 110)
        Label(self.make_canvas, text="Player 2", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=15,y=15+(40*6+40*3)+40 + 110+ 40)
        self.store_instructional_btn(block_predict_sky_blue, predict_sky_blue, entry_take_sky_blue, final_move)
    
# Lógica para o botão amarelo
    def instruction_btn_yellow(self):
        block_predict_yellow = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+10, y=15 + (40 * 6 + 40 * 3) + 10)
        predict_yellow = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Predict",font=("Arial", 8, "bold"), command=lambda: self.make_prediction("yellow"))
        predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+10, y=15 + (40 * 6 + 40 * 3) + 40 + 10)
        entry_take_yellow = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"),width=2, relief=SUNKEN, bd=5)
        entry_take_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+13, y=15 + (40 * 6 + 40 * 3) + 40 + 50)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Give",font=("Arial", 8, "bold"),command=lambda: self.main_controller("yellow",entry_take_yellow.get()),state=DISABLED)
        final_move.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+17, y=15 + (40 * 6 + 40 * 3) + 40 + 110)
        Label(self.make_canvas, text="Player 3", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 3),y=15 + (40 * 6 + 40 * 3) + 40 + 110 + 40)
        self.store_instructional_btn(block_predict_yellow, predict_yellow, entry_take_yellow, final_move)
    
# Lógica para o botão verde
    def instruction_btn_green(self):
        block_predict_green = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_green.place(x=100+(40*6+40*3+40*6+10)+10, y=15)
        predict_green = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Predict", font=("Arial", 8, "bold"), command=lambda: self.make_prediction("green"))
        predict_green.place(x=100+(40*6+40*3+40*6+2)+10, y=15 + 40)
        entry_take_green = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2, relief=SUNKEN, bd=5)
        entry_take_green.place(x=100+(40*6+40*3+40*6+2)+13, y=15 + 80)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Give",font=("Arial", 8, "bold"),command=lambda: self.main_controller("green",entry_take_green.get()),state=DISABLED)
        final_move.place(x=100+(40*6+40*3+40*6+2)+17, y=15 + 140)
        Label(self.make_canvas, text="Player 4", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=100+(40*6+40*3+40*6+3), y=15 + 140+40)
        self.store_instructional_btn(block_predict_green, predict_green, entry_take_green, final_move)

# Lógica para armazenar botões 
    def store_instructional_btn(self, block_indicator, predictor, entry_controller, give_finally):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        temp.append(give_finally)
        self.block_value_predict.append(temp)
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

# Lógica para a personalização dinâmica dos botões com base na situação atual
    def instructional_btn_customization_based_on_current_situation(self, color_indicator, permanent_block_number, block_value_predict):
        if color_indicator == "red":
            temp_coin_position = self.red_coin_position
        elif color_indicator == "green":
            temp_coin_position = self.green_coin_position
        elif color_indicator == "yellow":
            temp_coin_position = self.yellow_coin_position
        else:
            temp_coin_position = self.sky_blue_coin_position

        all_in = 1
        for i in range(4):
            if temp_coin_position[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if permanent_block_number == 6:
            self.six_counter += 1
        else:
            self.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in == 0)) and self.six_counter < 3:
            permission = 1
            if color_indicator == "red":
                temp = self.red_coord_store
            elif color_indicator == "green":
                temp = self.green_coord_store
            elif color_indicator == "yellow":
                temp = self.yellow_coord_store
            else:
                temp = self.sky_blue_coord_store

            if permanent_block_number < 6:
                if self.six_with_overlap == 1:
                    self.time_for -= 1
                    self.six_with_overlap = 0
                for i in range(4):
                    if temp[i] == -1:
                        permission = 0
                    elif temp[i] > 100:
                        if temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            else:
                for i in range(4):
                    if temp[i] > 100:
                        if temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.make_command()
            else:
                block_value_predict[3]['state'] = NORMAL  # Give btn activation
                block_value_predict[1]['state'] = DISABLED  # Predict btn deactivation

        else:
            block_value_predict[1]['state'] = NORMAL  # Predict btn activation
            if self.six_with_overlap == 1:
                self.time_for -= 1
                self.six_with_overlap = 0
            self.make_command()

        if permanent_block_number == 6 and self.six_counter < 3 and block_value_predict[3]['state'] == NORMAL:
            self.time_for -= 1
        else:
            self.six_counter = 0
