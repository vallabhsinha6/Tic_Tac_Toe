import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]  
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [
            tk.Button(self.root, text=" ", font=('Arial', 20), width=5, height=2, command=lambda i=i: self.make_move(i))
            for i in range(9)
        ]

        for row in range(3):
            for col in range(3):
                index = row * 3 + col
                self.buttons[index].grid(row=row, column=col)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                self.show_winner()
            elif " " not in self.board:
                self.show_draw()
            else:
                self.switch_player()
                if self.current_player == "O":
                    self.ai_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        _, best_move = self.minimax(self.board, True)
        self.make_move(best_move)

    def minimax(self, board, maximizing_player, depth=0, alpha=float('-inf'), beta=float('inf')):
        scores = {'X': -1, 'O': 1, 'tie': 0}

        winner = self.check_winner(board)
        if winner:
            return scores[winner], None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    eval_score, _ = self.minimax(board, False, depth + 1, alpha, beta)
                    board[i] = " "  

                    if eval_score > max_eval:
                        max_eval = eval_score
                        best_move = i

                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    eval_score, _ = self.minimax(board, True, depth + 1, alpha, beta)
                    board[i] = " "  

                    if eval_score < min_eval:
                        min_eval = eval_score
                        best_move = i

                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break

            return min_eval, best_move

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                return board[combo[0]]

        if " " not in board:
            return "tie"

        return None

    def show_winner(self):
        winner = self.current_player
        tk.messagebox.showinfo("Round Over", f"{winner} wins!")
        self.reset_game()

    def show_draw(self):
        tk.messagebox.showinfo("Round Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL)
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.ai_move()  

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
