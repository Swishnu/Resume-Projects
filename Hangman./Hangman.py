import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word


def game(word):
    full_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Let's start guessing!")
    print(display_hangman(tries))
    print(full_word)
    print("\n")

    while not guessed and tries > 0:
        guess = input("What are you guessing: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already used", guess)
            elif guess not in word:
                print("Unlucky!")
                tries -= 1
                print("You have ", tries, "tries left")
                guessed_letters.append(guess)
            else:
                print("NICE!, that's right")
                guessed_letters.append(guess)
                words_in_list = list(full_word)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    words_in_list[index] = guess
                    full_word = "".join(words_in_list)
                if "_" not in words_in_list:
                    guessed = True
        elif len(guess) is len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Already guessed ", guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                full_word = word
        else:
            print("Try again")
        print(display_hangman(tries))
        print(full_word)
        print("\n")
    if guessed:
        print("Congrats you've completed the word! You Win!")
    else:
        print("Sorry you lost. The word was ", word)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        game(word)


if __name__ == "__main__":
    main()
