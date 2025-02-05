#creating tic tac toe game

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

turn = "X"
count = 0
buttons = [[None, None, None], [None, None, None], [None, None, None]]

def check_winner():
    global buttons
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    return None

def on_click(row, col):
    global turn, count
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = turn
        count += 1
        winner = check_winner()
        if winner is not None:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            root.destroy()
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            root.destroy()
        turn = "O" if turn == "X" else "X"

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=10, height=3,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()