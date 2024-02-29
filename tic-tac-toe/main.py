import tkinter as tk
from tkinter import messagebox

class Tic:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.player = "X"
        self.board = [[" "]*3 for _ in range(3)]
        self.buttons = []  # to store buttons
        for i in range(3):
            row_buttons = []  # for each row
            for j in range(3):
                button = tk.Button(window, text=" ", font=("Helvetica", 20), width=6, height=3)
                button.config(command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.player} wins")
                self.clear_board()
            elif all([symbol != " " for row in self.board for symbol in row]):
                messagebox.showinfo("Tie")
                self.clear_board()
            
        else:
            messagebox.showerror("Invalid Move")

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if all([self.board[i][j] == self.player for j in range(3)]) \
                    or all([self.board[j][i] == self.player for j in range(3)]):
                return True

        # Check diagonals
        main_diag_win = all([self.board[i][i] == self.player for i in range(3)])
        secondary_diag_win = all([self.board[i][2 - i] == self.player for i in range(3)])
        if main_diag_win or secondary_diag_win:
            return True

        return False

    def clear_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ")
        self.player = "X"

window = tk.Tk()
app = Tic(window)
window.mainloop()
