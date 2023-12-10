import random
#a collection of puzzles
word_list = ["konfabulacja", "transcendencja", "agnostyk", "kwant", "fizyka", "oppenheimer"]

chosen_word = random.choice(word_list)
mistake = 0
display = []

for i in chosen_word:
    display.append("_")

converted_display = map(str, display)
display_start = ''.join(converted_display)
print(display_start)

#show me the positions (indexes) of the guessed letter
def indexes(iterable, obj):
    for index, elem in enumerate(iterable):
        if elem == obj:
            yield index

#enter a letter. if it is correct, check indexes
def guess_function():
    guess = input("Guess a letter: ").lower()

    idxs = indexes(chosen_word, guess[0])
    result = list(idxs)

    #if the user types multiple letters, take only the first one.
    for letter in range (len(result)):
            display[result[letter]] = guess[0]

    return guess[0]

#defined levels of hangman
def draw_hangman(mistake):
    hangman_art = [
        """
        ------
        |    |
        |
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        """
    ]

    return hangman_art[mistake]

while mistake < 6:
    guessed_letter = guess_function()

    #draw a level of hangman if typed letter is incorrect
    if guessed_letter not in chosen_word:
        mistake += 1
        print(f"Mistake nr: {mistake}")
        print(draw_hangman(mistake))

    #update the puzzle and show
    converted_display = map(str, display)
    puzzle = ''.join(converted_display)
    print(puzzle)

    if chosen_word == puzzle:
        print("Yeah, YOU WON! Grats!")
        break

if mistake == 6:
    print("You lost :( \nTry again! :)")
