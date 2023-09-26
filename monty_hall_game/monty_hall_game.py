"""
Program: monty_hall_game.py
Author: Jack Aden
Last date modified: 12/10/2022

Write a GUI that runs the monty hall problem a set amount of time to get data on best solution to stay with choice or
switch.
"""
#import libraries
import random
import tkinter as tk
from tkinter import *




#Create function for host to reveal door that doesn't contain the prize and a door that isn't the player org choice
def get_non_prize_door(host, num_doors, player_choice):
    i = 1
    while i == host or i == player_choice:
        i = (i+1) % num_doors

    return i


#Create a function to have the player switch to the other unopened door
def switch_function(shown_door, num_doors, player_choice):
    i = 1
    while i == shown_door or i == player_choice:
        i = (i+1) % num_doors

    return i


#Create a function to simulate the game
def monty_hall_game(switch, num_tests):

    win_switch_cnt = 0
    win_no_switch_cnt = 0
    lose_switch_cnt = 0
    lose_no_switch_cnt = 0


    doors = [0, 1, 2]#doors as list
    num_doors = len(doors)

    #Loop through the number of times the player can play through the game
    for i in range(0, num_tests):
        door_with_prize = random.randint(0, num_doors-1)#Randomly choose a door between [0,2]
        host = door_with_prize
        player_choice = random.randint(0, num_doors-1)
        original_player_choice = player_choice
        shown_door = get_non_prize_door(host, num_doors, player_choice)

        #if the player chooses to always switch, then allow to switch their original chosen door to other unopened
        if switch is True:
            player_choice = switch_function(shown_door, num_doors, player_choice)

        if player_choice == door_with_prize and switch == False:
            #Then the player wins from not switching
            print("Player wins (No switch) - The player chose door: ", player_choice, "Original door choice:", original_player_choice, "Door with prize:", door_with_prize, "Shown door:", shown_door)
            win_no_switch_cnt = win_no_switch_cnt + 1
        elif player_choice == door_with_prize and switch == True:
            #Then the player wins from switching
            print("Player wins (Switch) - The player chose door: ", player_choice, "Original door choice:", original_player_choice, "Door with prize:", door_with_prize, "Shown door:", shown_door)
            win_switch_cnt = win_switch_cnt + 1
        elif player_choice != door_with_prize and switch == False:
            #Then the player lost from not switching
            print("Player lost (No switch) - The player chose door: ", player_choice, "Original door choice:", original_player_choice, "Door with prize:", door_with_prize, "Shown door:", shown_door)
            lose_no_switch_cnt = lose_no_switch_cnt + 1
        elif player_choice != door_with_prize and switch == True:
            #Then the player lost from switching
            print("Player lost (Switch) - The player chose door: ", player_choice, "Original door choice:", original_player_choice, "Door with prize:", door_with_prize, "Shown door:", shown_door)
            lose_switch_cnt = lose_switch_cnt + 1
        else:
            print("Error")

    return win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt, num_tests


def run_mhp():
    switch_y_n = bool(entry1.get())
    if not type(switch_y_n) is bool:
        raise TypeError("Enter True for switch or leave line blank for stay")
    num_test = int(entry2.get())
    if not type(num_test) is int:
        raise TypeError("Only numbers allowed")
    x = monty_hall_game(switch_y_n, num_test)
    label = Label(root, text="Result: " + str(x))
    label.grid(row=4)
    label2 = Label(root, text="Win switch: " + str(x[1]/x[4]))
    label2.grid(row=5)
    label3 = Label(root, text="Lose switch: " + str(x[3]/x[4]))
    label3.grid(row=6)
    label4 = Label(root, text="Win no-switch: " + str(x[0]/x[4]))
    label4.grid(row=7)
    label5 = Label(root, text="Lost no-switch: " + str(x[2]/x[4]))
    label5.grid(row=8)



root = tk.Tk()
root.geometry("1200x1200")
game = Label(root, text="This is a GUI to run the monty hall problem a different amount of times "
                            "to see if it is bette to stay with original choice or switch")
game.grid(row=0)
t_f_label = Label(root, text="Enter: True if you want to switch. Leave line blank if you want to stay")
t_f_label.grid(row=1)
num = Label(root, text="Enter a number of how many times you want to run the problem. eg 10")
num.grid(row=2)
entry1 = Entry(root)
entry1.grid(row=1, column=1)
entry2 = Entry(root)
entry2.grid(row=2, column=1)

button = Button(root, text="Play", command=run_mhp)
button.grid(row=3)

root.mainloop()


