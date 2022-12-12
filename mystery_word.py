import random


def play_game():
    # open the file and choose a word
    with open('words.txt') as my_list:
        read_list = my_list.read()
    with open('win.txt') as win_message:
        win_msg = win_message.read()
    with open('lose.txt') as lose_message:
        lose_msg = lose_message.read()
    with open('intro.txt') as intro_message:
        intro_msg = intro_message.read()
    # takes all words and convert to list
    split_list = read_list.split()
    print(intro_msg)
    # pick random word
    my_word = random.choice(split_list)
    print(my_word)
    guesses = []
    blanks = []
    my_letters = [*my_word]
    for letter in my_letters:
        blanks.append('_')
    print(*blanks)

    lifelines = 8

    while lifelines > 0 and blanks != my_letters:
        # loop player in game
        guess = input('Guess a letter ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print(f'\n{guess} is an invalid input\n')
        elif guess in guesses or guess in blanks:
            print(f'{guess} has already been guessed\n')

        elif guess in my_letters:
            print('Good guess!\n')

            for index, letter in enumerate(my_letters):
                if guess == letter:
                    blanks[index] = guess
        else:
            guesses.append(guess)
            unpacked_guesses = ', '.join(guesses)
            lifelines -= 1
            print(f'Sorry try again \nLives left: {lifelines}')

        unpacked_blanks = ' '.join(blanks)
        print(f'\n{unpacked_blanks}\n')
        if len(guesses) > 0:
            print(f'\nWrong letters: {unpacked_guesses}')
    if lifelines > 0:
        print(f'Congrats, you win!!!! \n{win_msg}')
    else:
        print(f'{lose_msg}')


if __name__ == "__main__":
    play_game()
    play_again = input('\nDo you want to play again? y/n ')
    while play_again == 'y':
        play_game()
        play_again = input('\nDo you want to play again? y/n ')
    print('Goodbye!')
