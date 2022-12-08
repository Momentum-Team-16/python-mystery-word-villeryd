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
    # while lifelines > 0:
    # loop player in game
    guess = input('guess a letter ')
    print(f'guess = {guess}')
    # for letter in my_word:
    # my_letters.append(letter)
    if guess in my_letters:
        print('DOPE, you guess good boi')

    print(my_letters)


if __name__ == "__main__":
    play_game()
