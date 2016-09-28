import random

max_attempt = 8


def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
        words = [word for word in words.split('\n') if len(word) > 5]
    return words


def choose_random_word(words):
    ''' Choose random word from list '''
    return random.choice(words)


def hangman():

    word = choose_random_word(read_words())

    print(word)

    guess_word = ['_']*len(word)
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    pressed_letters = set()

    print('Welcome to the game, Hangman! \nI am thinking of a word that is %i \n letters long.' % len(word))
    print('-'*6)

    counter = 0

    while counter < max_attempt:
        print('You have %i guesses left' % (max_attempt - counter))
        print('Available letters:' + available_letters)

        guess = input('Please guess a letter:')

        if guess in word and guess in available_letters and guess != '':
            # pressed character presents in word
            # get char positions in word
            indexes = [i for (i, ltr) in enumerate(word) if ltr == guess]

            # put char into guessed word
            for i in indexes:
                guess_word[i] = guess
            print('Good guess: %s \n' % ''.join(guess_word))
        elif guess in pressed_letters and guess != '':
            # pressed char not present in word or already pressed
            print('Invalid letter, please try again. \n')
        else:
            # else increment attempt
            print('Oops! That letter is not in my word: %s \n' % ''.join(guess_word))
            counter += 1

        if word == ''.join(guess_word):
            print('You win!')
            break

        pressed_letters.add(guess)
        available_letters = available_letters.replace(guess, '')

    if word != ''.join(guess_word):
        print('Sorry, but you lost.')

    print('The word I am thinking is \'%s\'' % word)


if __name__ == '__main__':

    hangman()
