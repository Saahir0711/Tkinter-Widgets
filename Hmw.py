from tkinter import *
import random

user_input = ""

def change_user_input(input):
    user_input = input

def topwin():
    top = Toplevel()
    top.geometry("500x500")
    top.title("toplevel")
    top.mainloop()
    

Window = Tk()
Window.geometry("700x800")
label = Label(text = "Choose rock paper or scissors", bg = "white",fg = "black", height = 3, width = 70)

paper = Button(text = "paper", fg = "black", bg = "white", command = change_user_input("paper"), height= "10", width = "70", )
scissors = Button(text = "scissors", fg = "black", bg = "white", command = change_user_input("scissors"), height= "10", width = "70")
rock = Button(text = "rock", fg = "black", bg = "white", command = change_user_input("rock"), height= "10", width = "70")

label.pack()
paper.pack()
scissors.pack()
rock.pack()


Window.mainloop()


num = random.randint(0,2)
choices = ["rock", "paper", "scissors"]
computer_input = choices[num]

if computer_input == user_input:
    label2 = Label(top, text = "You won!", height = "50", width = "70")
elif user_input == "rock" and computer_input == "scissors":
    label2 = Label(top, text = "You won!", height = "50", width = "70")
elif user_input == "paper" and computer_input == "rock":
    label2 = Label(top, text = "You won!", height = "50", width = "70")
elif user_input == "scissors" and computer_input == "paper":
    label2 = Label(top, text = "You won!", height = "50", width = "70")
else:
    label2 = Label(top, text = "You lost.", height = "50", width = "70")

label2.pack()
