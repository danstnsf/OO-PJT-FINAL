from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint

class Controles():
    def take_initial_control(self):
        for i in range(4):
            self.block_value_predict[i][1]['state'] = DISABLED

        # COnfigurar numero de jogadores
        top = Toplevel()
        top.geometry("600x150")
        top.maxsize(600,150)
        top.minsize(600,150)
        top.config(bg="orange")
        top.iconbitmap("Images/ludo_icon.ico")

        head = Label(top,text="-:Numero de Jogadores:- ",font=("Arial",25,"bold","italic"),bg="orange",fg="chocolate")
        head.place(x=70,y=30)
        take_entry = Entry(top,font=("Arial",18,"bold","italic"),relief=SUNKEN,bd=7,width=12)
        take_entry.place(x=150,y=80)
        take_entry.focus()

        def filtering():
            response_take = self.input_filtering(take_entry.get())
            if response_take is True and int(take_entry.get())>1:
                for player_index in range(int(take_entry.get())):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)
                self.make_command()
                top.destroy()
            else:
                messagebox.showerror("Input Error", "Por favor insira um numero entre 2 e 4")

        submit_btn = Button(top,text="Enviar",bg="black",fg="#00FF00",font=("Arial",13,"bold"),relief=RAISED,bd=8,command=filtering)
        submit_btn.place(x=350,y=80)
        top.mainloop()

    # Jogar dados
    def make_prediction(self,color_indicator):
        try:
            if color_indicator == "red":
                block_value_predict = self.block_value_predict[0]
                permanent_block_number = self.move_red_counter = randint(1, 6)

            elif color_indicator == "sky_blue":
                block_value_predict = self.block_value_predict[1]
                permanent_block_number = self.move_sky_blue_counter = randint(1, 6)

            elif color_indicator == "yellow":
                block_value_predict = self.block_value_predict[2]
                permanent_block_number = self.move_yellow_counter = randint(1, 6)

            else:
                block_value_predict = self.block_value_predict[3]
                permanent_block_number = self.move_green_counter = randint(1, 6)


            block_value_predict[1]['state'] = DISABLED

            # animacao da moeda
            temp_counter = 15
            while temp_counter>0:
                move_temp_counter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
                self.window.update()
                time.sleep(0.1)
                temp_counter-=1

            print("Prediction result: ", permanent_block_number)

          
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1]
            self.instructional_btn_customization_based_on_current_situation(color_indicator,permanent_block_number,block_value_predict)
        except:
            print("Force stop error")

    def instructional_btn_customization_based_on_current_situation(self,color_indicator,permanent_block_number,block_value_predict):
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

        if  permanent_block_number == 6:
            self.six_counter += 1
        else:
            self.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in==0)) and self.six_counter<3:
            permission = 1
            if color_indicator == "red":
                temp = self.red_coord_store
            elif color_indicator == "green":
                temp = self.green_coord_store
            elif color_indicator == "yellow":
                temp = self.yellow_coord_store
            else:
                temp = self.sky_blue_coord_store

            if  permanent_block_number<6:
                if self.six_with_overlap == 1:
                    self.time_for-=1
                    self.six_with_overlap=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i]+permanent_block_number<=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + permanent_block_number <= 106:
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
                block_value_predict[3]['state'] = NORMAL# ativar botao do dado
                block_value_predict[1]['state'] = DISABLED# desativar botao do dado

        else:
            block_value_predict[1]['state'] = NORMAL# ativar botao do dado
            if self.six_with_overlap == 1:
                self.time_for -= 1
                self.six_with_overlap = 0
            self.make_command()

        if  permanent_block_number == 6 and self.six_counter<3 and block_value_predict[3]['state'] == NORMAL:
            self.time_for-=1
        else:
            self.six_counter=0

    # controle de jogadas
    def make_command(self):
        if  self.time_for == -1:
            pass
        else:
            self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if  self.time_for == len(self.total_people_play)-1:
            self.time_for = -1

        self.time_for+=1
        self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = NORMAL


    def instruction_btn_red(self):
        block_predict_red = Label(self.make_canvas,image=self.block_number_side[0])
        block_predict_red.place(x=45,y=15)
        predict_red = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Jogar dado", font=("Arial", 8, "bold"), command=lambda: self.make_prediction("red"))
        predict_red.place(x=37, y=15 + 40)
        entry_take_red = Entry(self.make_canvas,bg="white",fg="blue",font=("Arial",25,"bold","italic"),width=2,relief=SUNKEN,bd=5)
        entry_take_red.place(x=40,y=15+80)
        final_move = Button(self.make_canvas,bg="black",fg="#00FF00",relief=RAISED,bd=5,text="Andar",font=("Arial",8,"bold"),command=lambda: self.main_controller("red",entry_take_red.get()),state=DISABLED)
        final_move.place(x=42,y=15+140)
        Label(self.make_canvas,text="Player 1",bg="#4d4dff",fg="gold",font=("Arial",15,"bold")).place(x=15,y=15+140+40)
        self.store_instructional_btn(block_predict_red,predict_red,entry_take_red,final_move)

    def instruction_btn_sky_blue(self):
        block_predict_sky_blue = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_sky_blue.place(x=45, y=15+(40*6+40*3)+10)
        predict_sky_blue = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Jogar dado",font=("Arial", 8, "bold"), command=lambda: self.make_prediction("sky_blue"))
        predict_sky_blue.place(x=37, y=15+(40*6+40*3)+40 + 10)
        entry_take_sky_blue = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2,relief=SUNKEN, bd=5)
        entry_take_sky_blue.place(x=40, y=15+(40*6+40*3)+40 + 50)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Andar", font=("Arial", 8, "bold"),command=lambda: self.main_controller("sky_blue",entry_take_sky_blue.get()),state=DISABLED)
        final_move.place(x=42, y=15+(40*6+40*3)+40 + 110)
        Label(self.make_canvas, text="Player 2", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=15,y=15+(40*6+40*3)+40 + 110+ 40)
        self.store_instructional_btn(block_predict_sky_blue, predict_sky_blue, entry_take_sky_blue, final_move)

    def instruction_btn_yellow(self):
        block_predict_yellow = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+10, y=15 + (40 * 6 + 40 * 3) + 10)
        predict_yellow = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Jogar dado",font=("Arial", 8, "bold"), command=lambda: self.make_prediction("yellow"))
        predict_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+10, y=15 + (40 * 6 + 40 * 3) + 40 + 10)
        entry_take_yellow = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"),width=2, relief=SUNKEN, bd=5)
        entry_take_yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+13, y=15 + (40 * 6 + 40 * 3) + 40 + 50)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Andar",font=("Arial", 8, "bold"),command=lambda: self.main_controller("yellow",entry_take_yellow.get()),state=DISABLED)
        final_move.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+17, y=15 + (40 * 6 + 40 * 3) + 40 + 110)
        Label(self.make_canvas, text="Player 3", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 3),y=15 + (40 * 6 + 40 * 3) + 40 + 110 + 40)
        self.store_instructional_btn(block_predict_yellow, predict_yellow, entry_take_yellow, final_move)

    def instruction_btn_green(self):
        block_predict_green = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_green.place(x=100+(40*6+40*3+40*6+10)+10, y=15)
        predict_green = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Jogar dado", font=("Arial", 8, "bold"), command=lambda: self.make_prediction("green"))
        predict_green.place(x=100+(40*6+40*3+40*6+2)+10, y=15 + 40)
        entry_take_green = Entry(self.make_canvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2, relief=SUNKEN, bd=5)
        entry_take_green.place(x=100+(40*6+40*3+40*6+2)+13, y=15 + 80)
        final_move = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Andar",font=("Arial", 8, "bold"),command=lambda: self.main_controller("green",entry_take_green.get()),state=DISABLED)
        final_move.place(x=100+(40*6+40*3+40*6+2)+17, y=15 + 140)
        Label(self.make_canvas, text="Player 4", bg="#4d4dff", fg="gold", font=("Arial", 15, "bold")).place(x=100+(40*6+40*3+40*6+3), y=15 + 140+40)
        self.store_instructional_btn(block_predict_green, predict_green, entry_take_green, final_move)


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


    def main_controller(self, color_coin, coin_number):
        processing_result = self.input_filtering(coin_number)
        if processing_result is True:
            pass
        else:
            messagebox.showerror("Input Error", "Coloque um número entre 1 e 4")
            return

        if  color_coin == "red":
            self.block_value_predict[0][3]['state'] = DISABLED

            if self.move_red_counter == 106:
                messagebox.showwarning("Chegou ao fim","Chegou ao destino")

            elif self.red_coin_position[int(coin_number)-1] == -1 and self.move_red_counter == 6:
                self.red_circle_start_position(coin_number)
                self.red_coord_store[int(coin_number) - 1] = 1

            elif self.red_coin_position[int(coin_number)-1] > -1:
                take_coord = self.make_canvas.coords(self.made_red_coin[int(coin_number)-1])
                red_start_label_x = take_coord[0] + 10
                red_start_label_y = take_coord[1] + 5
                self.red_number_label[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_coin_position[int(coin_number)-1]+self.move_red_counter<=106:
                   self.red_coin_position[int(coin_number)-1] = self.motion_of_coin(self.red_coin_position[int(coin_number) - 1],self.made_red_coin[int(coin_number)-1],self.red_number_label[int(coin_number)-1],red_start_label_x,red_start_label_y,"red",self.move_red_counter)
                else:
                   messagebox.showerror("impossivel","nao permitido")
                   self.block_value_predict[0][3]['state'] = NORMAL
                   return

                if  self.red_coin_position[int(coin_number)-1]==22 or self.red_coin_position[int(coin_number)-1]==9 or self.red_coin_position[int(coin_number)-1]==48 or self.red_coin_position[int(coin_number)-1]==35 or self.red_coin_position[int(coin_number)-1]==14 or self.red_coin_position[int(coin_number)-1]==27 or self.red_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.red_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.red_coin_position[int(coin_number)-1],color_coin, self.move_red_counter)

                self.red_coord_store[int(coin_number)-1] = self.red_coin_position[int(coin_number)-1]

            else:
                messagebox.showerror("Errado","Seu peao nao pode mover")
                self.block_value_predict[0][3]['state'] = NORMAL
                return

            self.block_value_predict[0][1]['state'] = NORMAL


        elif color_coin == "green":
            self.block_value_predict[3][3]['state'] = DISABLED

            if self.move_green_counter == 106:
                messagebox.showwarning("Chegou ao fim","Chegou ao destino")

            elif self.green_coin_position[int(coin_number) - 1] == -1 and self.move_green_counter == 6:
                self.green_circle_start_position(coin_number)
                self.green_coord_store[int(coin_number) - 1] = 14

            elif self.green_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_green_coin[int(coin_number) - 1])
                green_start_label_x = take_coord[0] + 10
                green_start_label_y = take_coord[1] + 5
                self.green_number_label[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)


                if  self.green_coin_position[int(coin_number) - 1] + self.move_green_counter <= 106:
                    self.green_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.green_coin_position[int(coin_number) - 1], self.made_green_coin[int(coin_number) - 1], self.green_number_label[int(coin_number) - 1], green_start_label_x, green_start_label_y, "green", self.move_green_counter)
                else:
                   messagebox.showerror("impossivel","nao permitido")
                   self.block_value_predict[3][3]['state'] = NORMAL
                   return


                if  self.green_coin_position[int(coin_number)-1]==22 or self.green_coin_position[int(coin_number)-1]==9 or self.green_coin_position[int(coin_number)-1]==48 or self.green_coin_position[int(coin_number)-1]==35 or self.green_coin_position[int(coin_number)-1]==1 or self.green_coin_position[int(coin_number)-1]==27 or self.green_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.green_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.green_coin_position[int(coin_number) - 1],color_coin, self.move_green_counter)

                self.green_coord_store[int(coin_number) - 1] = self.green_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("impossivel","nao permitido")
                self.block_value_predict[3][3]['state'] = NORMAL
                return

            self.block_value_predict[3][1]['state'] = NORMAL


        elif color_coin == "yellow":
            self.block_value_predict[2][3]['state'] = DISABLED

            if self.move_yellow_counter == 106:
                messagebox.showwarning("Chegou ao fim","Chegou ao destino")

            elif self.yellow_coin_position[int(coin_number) - 1] == -1 and self.move_yellow_counter == 6:
                self.yellow_circle_start_position(coin_number)
                self.yellow_coord_store[int(coin_number) - 1] = 27

            elif self.yellow_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_yellow_coin[int(coin_number) - 1])
                yellow_start_label_x = take_coord[0] + 10
                yellow_start_label_y = take_coord[1] + 5
                self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if  self.yellow_coin_position[int(coin_number) - 1] + self.move_yellow_counter <= 106:
                    self.yellow_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.yellow_coin_position[int(coin_number) - 1], self.made_yellow_coin[int(coin_number) - 1], self.yellow_number_label[int(coin_number) - 1], yellow_start_label_x, yellow_start_label_y, "yellow", self.move_yellow_counter)
                else:
                   messagebox.showerror("impossivel","nao permitido")
                   self.block_value_predict[2][3]['state'] = NORMAL
                   return

                if  self.yellow_coin_position[int(coin_number)-1]==22 or self.yellow_coin_position[int(coin_number)-1]==9 or self.yellow_coin_position[int(coin_number)-1]==48 or self.yellow_coin_position[int(coin_number)-1]==35 or self.yellow_coin_position[int(coin_number)-1]==1 or self.yellow_coin_position[int(coin_number)-1]==14 or self.yellow_coin_position[int(coin_number)-1]==40:
                    pass
                else:
                    if self.yellow_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.yellow_coin_position[int(coin_number) - 1],color_coin, self.move_yellow_counter)

                self.yellow_coord_store[int(coin_number) - 1] = self.yellow_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("impossivel","nao permitido")
                self.block_value_predict[2][3]['state'] = NORMAL
                return

            self.block_value_predict[2][1]['state'] = NORMAL


        elif color_coin == "sky_blue":
            self.block_value_predict[1][3]['state'] = DISABLED
            if self.move_red_counter == 106:
                messagebox.showwarning("Chegou ao fim","Chegou ao destino")

            elif self.sky_blue_coin_position[int(coin_number) - 1] == -1 and self.move_sky_blue_counter == 6:
                self.sky_blue_circle_start_position(coin_number)
                self.sky_blue_coord_store[int(coin_number) - 1] = 40

            elif self.sky_blue_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_sky_blue_coin[int(coin_number) - 1])
                sky_blue_start_label_x = take_coord[0] + 10
                sky_blue_start_label_y = take_coord[1] + 5
                self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

                if  self.sky_blue_coin_position[int(coin_number) - 1] + self.move_sky_blue_counter <= 106:
                    self.sky_blue_coin_position[int(coin_number) - 1] = self.motion_of_coin(self.sky_blue_coin_position[int(coin_number) - 1], self.made_sky_blue_coin[int(coin_number) - 1], self.sky_blue_number_label[int(coin_number) - 1], sky_blue_start_label_x, sky_blue_start_label_y, "sky_blue", self.move_sky_blue_counter)
                else:
                   messagebox.showerror("impossivel","nao permitido")
                   self.block_value_predict[1][3]['state'] = NORMAL
                   return

                if  self.sky_blue_coin_position[int(coin_number)-1]==22 or self.sky_blue_coin_position[int(coin_number)-1]==9 or self.sky_blue_coin_position[int(coin_number)-1]==48 or self.sky_blue_coin_position[int(coin_number)-1]==35 or self.sky_blue_coin_position[int(coin_number)-1]==1 or self.sky_blue_coin_position[int(coin_number)-1]==14 or self.sky_blue_coin_position[int(coin_number)-1]==27:
                    pass
                else:
                    if self.sky_blue_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.sky_blue_coin_position[int(coin_number) - 1],color_coin, self.move_sky_blue_counter)

                self.sky_blue_coord_store[int(coin_number) - 1] = self.sky_blue_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("impossivel","nao permitido")
                self.block_value_predict[1][3]['state'] = NORMAL
                return

            self.block_value_predict[1][1]['state'] = NORMAL

        print(self.red_coord_store)
        print(self.green_coord_store)
        print(self.yellow_coord_store)
        print(self.sky_blue_coord_store)

        permission_granted_to_proceed = True

        if  color_coin == "red" and self.red_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "green" and self.green_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "yellow" and self.yellow_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif  color_coin == "sky_blue" and self.sky_blue_coin_position[int(coin_number)-1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)

        if permission_granted_to_proceed:
            self.make_command()