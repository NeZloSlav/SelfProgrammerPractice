# Задание: игра "Виселица".

def hangman(word):
    mistake_count = 0
    stages = ["",
              "__________       ",
              "|                ",
              "|         |      ",
              "|         0      ",
              "|        /|\     ",
              "|        / \     ",
              "|                ",
              ]

    board = ["_"] * len(word)

    win = False
    print('Welcome to the execution')

    while mistake_count < len(stages) - 1:

        char = input('\nEnter the word: ')

        if char in word:
            print("Yup! You guessed!")

            char_index = word.index(char)
            board[char_index] = f"{char}"
        else:
            mistake_count += 1

        print(" ".join(board))
        print("\n".join(stages[:mistake_count + 1]))

        if "_" not in board:
            print("You win! The hidden word was: ")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[:mistake_count+1]))
        print("You lose. The hidden word was: ")
        print(" ".join(word))


hangman("кот")
