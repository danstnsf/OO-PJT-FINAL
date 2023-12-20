from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint

class Pawn():
    def motion_of_coin(self,counter_coin,specific_coin,number_label,number_label_x ,number_label_y,color_coin,path_counter):
        number_label.place(x=number_label_x,y=number_label_y)
        while True:
            if path_counter == 0:
                break
            elif (counter_coin == 51 and color_coin == "red") or (counter_coin==12 and color_coin == "green") or (counter_coin == 25 and color_coin == "yellow") or (counter_coin == 38 and color_coin == "sky_blue") or counter_coin>=100:
                if counter_coin<100:
                    counter_coin=100

                counter_coin = self.under_room_traversal_control(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin, color_coin)

                if  counter_coin == 106:
                    messagebox.showinfo("Destination reached","Congrats! You now at the destination")
                    if path_counter == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1
                break

            counter_coin += 1
            path_counter -=1
            number_label.place_forget()

            print(counter_coin)

            if counter_coin<=5:
                self.make_canvas.move(specific_coin, 40, 0)
                number_label_x+=40
            elif counter_coin == 6:
                self.make_canvas.move(specific_coin, 40, -40)
                number_label_x += 40
                number_label_y-=40
            elif 6< counter_coin <=11:
                self.make_canvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin <=13:
                self.make_canvas.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=18:
                self.make_canvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin == 19:
                self.make_canvas.move(specific_coin, 40, 40)
                number_label_x += 40
                number_label_y += 40
            elif counter_coin <=24:
                self.make_canvas.move(specific_coin, 40, 0)
                number_label_x += 40
            elif counter_coin <=26:
                self.make_canvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <=31:
                self.make_canvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin == 32:
                self.make_canvas.move(specific_coin, -40, 40)
                number_label_x -= 40
                number_label_y += 40
            elif counter_coin <= 37:
                self.make_canvas.move(specific_coin, 0, 40)
                number_label_y += 40
            elif counter_coin <= 39:
                self.make_canvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif counter_coin <= 44:
                self.make_canvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 45:
                self.make_canvas.move(specific_coin, -40, -40)
                number_label_x -= 40
                number_label_y -= 40
            elif counter_coin <= 50:
                self.make_canvas.move(specific_coin, -40, 0)
                number_label_x -= 40
            elif 50< counter_coin <=52:
                self.make_canvas.move(specific_coin, 0, -40)
                number_label_y -= 40
            elif counter_coin == 53:
                self.make_canvas.move(specific_coin, 40, 0)
                number_label_x += 40
                counter_coin = 1

            number_label.place_forget()
            number_label.place(x=number_label_x, y=number_label_y)

            self.window.update()
            time.sleep(0.2)

        return counter_coin

    # For same position, previous coin deleted and set to the room
    def coord_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
        if  color_coin!="red":
            for take_coin_number in range(len(self.red_coord_store)):
                if  self.red_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap=1
                    else:
                        self.time_for-=1

                    self.make_canvas.delete(self.made_red_coin[take_coin_number])
                    self.red_number_label[take_coin_number].place_forget()
                    self.red_coin_position[take_coin_number] = -1
                    self.red_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                       remade_coin = self.make_canvas.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red", outline="black")
                       self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.make_canvas.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="red", outline="black")
                        self.red_number_label[take_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                    self.made_red_coin[take_coin_number]=remade_coin

        if  color_coin != "green":
            for take_coin_number in range(len(self.green_coord_store)):
                if  self.green_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for-=1

                    self.make_canvas.delete(self.made_green_coin[take_coin_number])
                    self.green_number_label[take_coin_number].place_forget()
                    self.green_coin_position[take_coin_number] = -1
                    self.green_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="#00FF00", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
                        self.green_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
                    else:
                        remade_coin = self.make_canvas.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
                        self.green_number_label[take_coin_number].place(x=340+(40*3) + 40 + 10, y=15 + 40 + 100 + 5)

                    self.made_green_coin[take_coin_number] = remade_coin


        if  color_coin != "yellow":
            for take_coin_number in range(len(self.yellow_coord_store)):
                if  self.yellow_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.made_yellow_coin[take_coin_number])
                    self.yellow_number_label[take_coin_number].place_forget()
                    self.yellow_coin_position[take_coin_number] = -1
                    self.yellow_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3) + 40 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340+(40*3)+ 40 + 40+ 60 + 30, y=30 + (40*6)+(40*3)+40+100+10)
                    else:
                        remade_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow", outline="black")
                        self.yellow_number_label[take_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                    self.made_yellow_coin[take_coin_number] = remade_coin

        if  color_coin != "sky_blue":
            for take_coin_number in range(len(self.sky_blue_coord_store)):
                if  self.sky_blue_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.made_sky_blue_coin[take_coin_number])
                    self.sky_blue_number_label[take_coin_number].place_forget()
                    self.sky_blue_coin_position[take_coin_number] = -1
                    self.sky_blue_coord_store[take_coin_number]=-1

                    if take_coin_number == 0:
                        remade_coin = self.make_canvas.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 1:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="#04d9ff", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 +60 + 10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 2:
                        remade_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
                    else:
                        remade_coin = self.make_canvas.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="#04d9ff", outline="black")
                        self.sky_blue_number_label[take_coin_number].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+60+40+10)

                    self.made_sky_blue_coin[take_coin_number] = remade_coin


    def under_room_traversal_control(self,specific_coin,number_label,number_label_x,number_label_y,path_counter,counter_coin,color_coin):
        if color_coin == "red" and counter_coin >= 100:
            if int(counter_coin)+int(path_counter)<=106:
               counter_coin = self.room_red_traversal(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin)

        elif color_coin == "green" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_green_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "yellow" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_yellow_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "sky_blue" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_sky_blue_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        return counter_coin


    def room_red_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter>0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 40, 0)
            number_label_x+=40
            number_label.place(x=number_label_x,y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_green_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 0, 40)
            number_label_y += 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_yellow_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, -40, 0)
            number_label_x -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def room_sky_blue_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.make_canvas.move(specific_coin, 0, -40)
            number_label_y -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def check_winner_and_runner(self,color_coin):
        destination_reached = 0 # Check for all specific color coins
        if color_coin == "red":
            temp_store = self.red_coord_store
            temp_delete = 0# Player index
        elif color_coin == "green":
            temp_store = self.green_coord_store
            temp_delete = 3# Player index
        elif color_coin == "yellow":
            temp_store = self.yellow_coord_store
            temp_delete = 2# Player index
        else:
            temp_store = self.sky_blue_coord_store
            temp_delete = 1# Player index

        for take in temp_store:
            if take == 106:
                destination_reached = 1
            else:
                destination_reached = 0
                break

        if  destination_reached == 1:# If all coins in block reach to the destination, winner and runner check
            self.take_permission += 1
            if self.take_permission == 1:# Winner check
                messagebox.showinfo("Winner","Congrats! You are the winner")
            elif self.take_permission == 2:# 1st runner check
                messagebox.showinfo("Winner", "Wow! You are 1st runner")
            elif self.take_permission == 3:# 2nd runner check
                messagebox.showinfo("Winner", "Wow! You are 2nd runner")

            self.block_value_predict[temp_delete][1]['state'] = DISABLED
            self.total_people_play.remove(temp_delete)

            if len(self.total_people_play) == 1:
                messagebox.showinfo("Game Over","Good bye!!!!")
                self.block_value_predict[0][1]['state'] = DISABLED
                return False
            else:
                self.time_for-=1
        else:
            print("Winner not decided")

        return True

    # Input value checking
    def input_filtering(self,coin_number):
        try:
            if (4>=int(coin_number)>=1) or type(coin_number) == int:
                return True
            else:
                return False
        except:
            return False