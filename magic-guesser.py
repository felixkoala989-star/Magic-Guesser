import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# hide the boring grey window behind the popups
root = tk.Tk()
root.withdraw()

# start the game
messagebox.showinfo("System Message", "Welcome to Magic Guesser! Please sign in to continue.")

# get login stuff
my_user = simpledialog.askstring("Login", "Please enter your username:")
my_pass = simpledialog.askstring("Login", "Please enter your password:")

# if they press cancel on the box so the game doesnt crash
if my_user == None or my_pass == None:
    quit()

# SECRET ADMIN LOGIN!!!
if my_user == "azko" and my_pass == "elpepe":
    messagebox.showinfo("System Message", "Apros2yo4zadks1Mw3")
    quit() # end the program for admin

# normal player game part
ask_play = messagebox.askyesno("System Message", "Welcome, " + my_user + "! Do you want to play this game?")

if ask_play == False: # if they click no
    quit()
else:
    # they clicked yes!
    messagebox.showinfo("System Message", "Great! Get ready for the magic. I will ask you 5 questions.")
    
    food_ans = simpledialog.askstring("Question 1", "what is your favortite food?")
    
    # making variables for the other questions but not actually using them later lol
    num_ans = simpledialog.askstring("Question 2", "say a number 1 to 10")
    math_ans = simpledialog.askstring("Question 3", "multiply it by 10 and subtract 5 idk. what is it?")
    color_ans = simpledialog.askstring("Question 4", "say a random color")
    animal_ans = simpledialog.askstring("Question 5", "say an animal")

    # fake magic part to trick them
    messagebox.showinfo("System Message", "MAGIC! I read your mind... your favorite food is " + str(food_ans) + "!!")