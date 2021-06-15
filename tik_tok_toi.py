import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+500+200")
root.title("Tik Tak Toe")
root.configure(background='white')

tops = Frame(root, bg='Cadet Blue', pady=2, width=800, height=100, relief=RIDGE)
tops.grid(row=0, column=0)

lblTitle = Label(tops, font=('Arial', 50, 'bold'), text="Tik Tak Toe", bd=21, bg='Cadet Blue',
                 fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

mainFrame = Frame(root, bg='Powder Blue', width=800, height=500, relief=RIDGE)
mainFrame.grid(row=1, column=0)

leftFrame = Frame(mainFrame, bg='Cadet Blue', pady=2, padx=10, width=530, height=500, relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame = Frame(mainFrame, bg='Cadet Blue', pady=2, padx=10, width=350, height=500, relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1 = Frame(rightFrame, bg='Cadet Blue', pady=2, padx=10, width=350, height=200, relief=RIDGE)
rightFrame1.grid(row=0, column=0)

rightFrame2 = Frame(rightFrame, bg='Cadet Blue', pady=2, padx=10, width=350, height=200, relief=RIDGE)
rightFrame2.grid(row=1, column=0)

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

row = StringVar()
column = StringVar()
buttons = StringVar()
click = True


'''def minimax(self, player, depth=0):
    if player == "O":
        best = -10
    else:
        best = 10
    if self.complete():
        if self.getWinner() == "X":
            return -10 + depth, None
        elif self.getWinner() == "tie":
            return 0, None
        elif self.getWinner() == "O":
            return 10 - depth, None
    for move in self.getAvailableMoves():
        self.makeMove(move, player)
        val, _ = self.minimax(self.getEnemyPlayer(player), depth+1)
        print(val)

        self.makeMove(move, ".")

        if player == "O":
            if val > best:
                best, bestMove = val, move
        else:
            if val < best:
                best, bestMove = val, move

    return best, bestMove'''


def checker(button):
    global click
    if button["text"] == " " and click:
        button["text"] = "X"
        click = False
        scorekeeper()
    elif button["text"] == " " and not click:
        button["text"] = "O"
        click = True
        scorekeeper()


def scorekeeper():
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.configure(background="Blue")
        button2.configure(background="Blue")
        button3.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.configure(background="Blue")
        button5.configure(background="Blue")
        button6.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.configure(background="Blue")
        button8.configure(background="Blue")
        button9.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.configure(background="Blue")
        button4.configure(background="Blue")
        button7.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.configure(background="Blue")
        button5.configure(background="Blue")
        button8.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.configure(background="Blue")
        button6.configure(background="Blue")
        button9.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.configure(background="Blue")
        button5.configure(background="Blue")
        button9.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()
    if button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.configure(background="Blue")
        button5.configure(background="Blue")
        button7.configure(background="blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "Congratulations")
        reset()

    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.configure(background="red")
        button2.configure(background="red")
        button3.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()
    if button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "Congratulations")
        reset()


def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="white")
    button2.configure(background="white")
    button3.configure(background="white")
    button4.configure(background="white")
    button5.configure(background="white")
    button6.configure(background="white")
    button7.configure(background="white")
    button8.configure(background="white")
    button9.configure(background="white")


def newgame():
    reset()
    playerX.set(0)
    playerO.set(0)


lblplayerX = Label(rightFrame1, font=('arial', 40, 'bold'), text="Player X :", padx=2, pady=2,
                   bg="Cadet Blue")
lblplayerX.grid(row=1, column=0, sticky=W)

txtplayerX = Entry(rightFrame1, font=('arial', 40, 'bold'), textvariable=playerX, width=10,
                   fg="black").grid(row=1, column=1)

lblplayerO = Label(rightFrame1, font=('arial', 40, 'bold'), text="Player O :", padx=2, pady=2,
                   bg="Cadet Blue")
lblplayerO.grid(row=2, column=0, sticky=W)

txtplayerO = Entry(rightFrame1, font=('arial', 40, 'bold'), textvariable=playerO, width=10,
                   fg="black").grid(row=2, column=1)

btnReset = Button(rightFrame2, text="Reset", font=('Times', 40, 'bold'), height=1, width=20,
                  bg='white', command=lambda: reset())
btnReset.grid(row=1, column=0)

btnNewgame = Button(rightFrame2, text="New Game", font=('Times', 40, 'bold'), height=1, width=20,
                    bg='white', command=lambda: newgame())
btnNewgame.grid(row=2, column=0)

button1 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(leftFrame, text=" ", font=('Times', 26, 'bold'), height=3, width=8, bg='white',
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()
