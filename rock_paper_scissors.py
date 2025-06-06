import tkinter as tk
import random

def play(choice):
    user_choice.set(choice)
    comp = random.choice(['Rock', 'Paper', 'Scissors'])
    comp_choice.set(comp)
    if choice == comp:
        result.set("Tie")
    elif (choice == 'Rock' and comp == 'Scissors') or \
         (choice == 'Paper' and comp == 'Rock') or \
         (choice == 'Scissors' and comp == 'Paper'):
        result.set("You Win")
    else:
        result.set("You Lose")

root = tk.Tk()
root.title("Rock Paper Scissors")

user_choice = tk.StringVar()
comp_choice = tk.StringVar()
result = tk.StringVar()

tk.Label(root, text="Your Choice:").pack()
tk.Label(root, textvariable=user_choice).pack()
tk.Label(root, text="Computer's Choice:").pack()
tk.Label(root, textvariable=comp_choice).pack()
tk.Label(root, text="Result:").pack()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Rock", command=lambda: play('Rock')).pack()
tk.Button(root, text="Paper", command=lambda: play('Paper')).pack()
tk.Button(root, text="Scissors", command=lambda: play('Scissors')).pack()

root.mainloop()
