from tkinter import *
from tkinter.font import BOLD
import random

# Initialize the main window
root = Tk()
root.geometry("526x500")
root.title("*ROCK PAPER SCISSOR*")
root.resizable(0, 0)
root.configure(background="#ff3838")

# Function to handle the game logic
def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = ''

    # Game logic
    if player_choice == computer_choice:
        result = f"It's a Tie! You both chose {player_choice}."
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = f"You Win! {player_choice} beats {computer_choice}."
    else:
        result = f"You Lose! {computer_choice} beats {player_choice}."

    # Update the result label
    result_label.config(text=result)

# Create the frame for the title and use grid instead of pack
frame1 = Frame(root, bg="#ff3838")
frame1.grid(row=0, column=0, padx=10, pady=20, columnspan=3)

# Title label
title_label = Label(frame1, text="ROCK PAPER SCISSOR", font=("Arial", 18, BOLD), bg="yellow", fg="black", bd=5, relief="raised")
title_label.pack(pady=10)

# Result label to display the result of the game
result_label = Label(root, text='', bg='#0A044B', fg='white', width=35, height=4, bd=4, relief="solid")
result_label.grid(column=0, row=1, columnspan=3, pady=(10, 20))
result_label.config(font=('Verdana', 14, BOLD))

# Frame for buttons
frame2 = Frame(root, bg="#ff3838")
frame2.grid(row=2, column=0, columnspan=3, pady=(10, 10))

# Styling for buttons
button_style = {
    "font": ('Arial', 14, BOLD),
    "bg": '#FFD700',
    "fg": 'black',
    "activebackground": '#FFC107',
    "activeforeground": 'black',
    "width": 12,
    "height": 2,
    "bd": 4,
    "relief": "raised"
}

# Buttons for player's choices with consistent styling
rock_button = Button(frame2, text='Rock', command=lambda: play_game('Rock'), **button_style)
rock_button.grid(column=0, row=0, padx=10, pady=10)

paper_button = Button(frame2, text='Paper', command=lambda: play_game('Paper'), **button_style)
paper_button.grid(column=1, row=0, padx=10, pady=10)

scissors_button = Button(frame2, text='Scissors', command=lambda: play_game('Scissors'), **button_style)
scissors_button.grid(column=2, row=0, padx=10, pady=10)

# Add a footer label
footer_label = Label(root, text="Enjoy the game!", font=("Arial", 10, BOLD), bg="#ff3838", fg="white")
footer_label.grid(row=3, column=0, columnspan=3, pady=20)

# Run the main loop
root.mainloop()
