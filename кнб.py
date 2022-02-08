from tkinter import *
import random
import sys
import os

root = Tk()
root.title("камень, ножницы, бумага")
root.geometry("800x600")
root["bg"] = "#E6E6FA"


global victories, defeats, draws


victories = 0
defeats = 0
draws = 0


photo1 = PhotoImage(file = 'камень.png')
Label(root, image = photo1, borderwidth = 0, compound = "center", highlightthickness = 0, padx = 0, pady = 0).place(x = 290, y = 90)
photo2 = PhotoImage(file = 'ножницы.png')
Label(root, image = photo2, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 290, y = 250)
photo3 = PhotoImage(file = 'бумага.png')
Label(root, image = photo3, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 290, y = 410)


a = {1:"камень", 2:"ножницы", 3:"бумага"}


stone = Button(text = "камень",
             background = "#00FF00",
             foreground = "#000000",
             padx = "59",
             pady = "50",
             font = "Arial 14")
stone.place(x = 75, y = 70)

scissors = Button(text = "ножницы",
             background = "#00FF00",
             foreground = "#000000",
             padx = "50",
             pady = "50",
             font = "Arial 14")
scissors.place(x = 75, y = 230)

paper = Button(text = "бумага",
             background = "#00FF00",
             foreground = "#000000",
             padx = "60",
             pady = "50",
             font = "Arial 14")
paper.place(x = 75, y = 390)



text1 = Label(text = "сделайте выбор:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
text1.place(x = 110, y = 25)
text2 = Label(text = "выбор компьютера:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
text5 = Label(text = "*", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 40")
text6 = Label(text = "побед:", foreground = "#000000", background = "#E6E6FA", font = "Arial 20")
text6.place(x = 440, y = 380)
text7 = Label(text = "поражений:", foreground = "#000000", background = "#E6E6FA", font = "Arial 20")
text7.place(x = 440, y = 430)
text8 = Label(text = "ничьих:", foreground = "#000000", background = "#E6E6FA", font = "Arial 20")
text8.place(x = 440, y = 480)

def click_stone(event):
    bot = a[random.randint(1, 3)]
    a1 = {1:"ничья", 2:"вы победили", 3:"вы проиграли"}
    global victories, defeats, draws
    if bot == a[1]:
        bot1 = a1[1]
        draws += 1
    if bot == a[2]:
        bot1 = a1[2]
        victories += 1
    if bot == a[3]:
        bot1 = a1[3]
        defeats += 1
    text2.place(x = 430, y = 260)
    global text31
    text31 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text31.place(x = 430, y = 300)
    global text61
    text61 = Label(text = victories, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text61.place(x = 600, y = 380)
    global text62
    text71 = Label(text = defeats, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text71.place(x = 600, y = 430)
    global text63
    text81 = Label(text = draws, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text81.place(x = 600, y = 480)
    global text41
    text41 = Label(text = bot1, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    text41.place(x = 430, y = 104)
    text5.place(x = 30, y = 118)  
stone.bind("<Button-1>", click_stone)

def click_scissors(event):
    bot = a[random.randint(1, 3)]
    a2 = {1:"вы проиграли", 2:"ничья", 3:"вы победили"}
    global victories, defeats, draws
    if bot == a[1]:
        bot2 = a2[1]
        defeats += 1
    if bot == a[2]:
        bot2 = a2[2]
        draws += 1
    if bot == a[3]:
        bot2 = a2[3]
        victories += 1
    text2.place(x = 430, y = 260)
    global text32
    text32 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text32.place(x = 430, y = 300)
    global text61
    text61 = Label(text = victories, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text61.place(x = 600, y = 380)
    global text62
    text71 = Label(text = defeats, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text71.place(x = 600, y = 430)
    global text63
    text81 = Label(text = draws, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text81.place(x = 600, y = 480)
    global text42
    text42 = Label(text = bot2, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    text42.place(x = 430, y = 104)
    text5.place(x = 30, y = 278)    
scissors.bind("<Button-1>", click_scissors)

def click_paper(event):
    bot = a[random.randint(1, 3)]
    a3 = {1:"вы победили", 2:"вы проиграли", 3:"ничья"}
    global victories, defeats, draws
    if bot == a[1]:
        bot3 = a3[1]
        victories += 1
    if bot == a[2]:
        bot3 = a3[2]
        defeats += 1
    if bot == a[3]:
        bot3 = a3[3]
        draws += 1
    text2.place(x = 430, y = 260)
    global text33
    text33 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text33.place(x = 430, y = 300)
    text61 = Label(text = victories, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text61.place(x = 600, y = 380)
    global text62
    text71 = Label(text = defeats, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text71.place(x = 600, y = 430)
    global text63
    text81 = Label(text = draws, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")   
    text81.place(x = 600, y = 480)
    global text43
    text43 = Label(text = bot3, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    text43.place(x = 430, y = 104)
    text5.place(x = 30, y = 438)
paper.bind("<Button-1>", click_paper)

def close():
    text2.place_forget()
    text5.place_forget()
    text31.place_forget()
    text41.place_forget()    
    text32.place_forget()
    text42.place_forget()    
    text33.place_forget()
    text43.place_forget()

new_game = Button(root, text = "новая игра",
             background = "#FFFF00",
             foreground = "#000000",
             padx = "32",
             pady = "16",
             font = "Arial 14",
             command = close)
new_game.place(x = 500, y = 30)

root.mainloop()
