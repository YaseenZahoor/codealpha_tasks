import random
hangman_stages = [
    """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |   |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |  /|
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |  /
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        |
        |
        |
        --------
        """
]
words_list=["APPLE","COMPUTER","HERO","FINISH","SUCCESS","BOOK","NOVEL","SEASON","SPRING"]
lives=6
display=[]
print("Welcome To hangman game \nNote: You have only 6 lives")
chosen_word=random.choice(words_list)
for i in range(len(chosen_word)):
    display+=("_")
print(' '.join(display))
game_finish=False
while not game_finish:
    guess=input("Enter a word to guess: ").upper()
    for index in range(len(chosen_word)):
        letter=chosen_word[index]
        if letter==guess:
            display[index]=guess
    for char in display:
        print(char, end=' ')
    print()
    if guess not in chosen_word:
        lives-=1
        print(hangman_stages[6-lives])
        if lives==0:
            game_finish=True
            print("You lose!")
    if "_" not in display:
        game_finish=True
        print("You win!")
