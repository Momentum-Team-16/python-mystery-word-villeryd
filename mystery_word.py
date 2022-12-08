import random


def play_game():
    # open the file and choose a word
    with open('words.txt') as my_list:
        read_list = my_list.read()
    split_list = read_list.split()
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
        elif guess in blanks:
            print(f'{guess} has already been guessed\n')

        elif guess in my_letters:
            print('DOPE, you guess good boi\n')

            for index, letter in enumerate(my_letters):
                if guess == letter:
                    blanks[index] = guess
        else:
            lifelines -= 1
            print(f'sorry try again \nLives left: {lifelines}')

        print('\n')
        print(*blanks)
        print('\n')


if __name__ == "__main__":
    play_game()
