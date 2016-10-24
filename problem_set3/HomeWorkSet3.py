import random
from itertools import permutations

HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
    'z': 10}


def get_word_score(word, HAND_SIZE):
    sum = 0
    for char in word:
        sum += SCRABBLE_LETTER_VALUES.get(char, 0)
    sum *= len(word)
    if len(word) == HAND_SIZE:
        sum += 50   # bonus for using all letters
    return sum


def get_frequancy_dict(hand):
    dic = {}
    for char in hand:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    return dic


def display_hand(hand):
    str = ''
    for (k, v) in hand.items():  # todo sort
        str += k*v
    return str


def update_hand(hand, word):
    new_hand = hand.copy()  # make a copy
    for ch in word:
        new_hand[ch] = new_hand.get(ch) - 1
        if new_hand[ch] < 0:
            raise ValueError('Wrong word')
    return new_hand


def generate_hand(n):
    hand = {}
    for i in range(n):
        key = random.choice(list(SCRABBLE_LETTER_VALUES.keys()))
        # print(key, '')
        if key in hand:
            hand[key] += 1
        else:
            hand.update({key: 1})
    return hand


def load_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    print('Loading word list from file...')
    with open(filename) as words_file:
        words = words_file.read()
        words = [word for word in words.split('\n') if len(word) > 2]
    print('  %i words loaded.' % len(words))
    return words


def is_valid_word(words, word, hand):
    '''    Check if word exist     '''
    if len(word) == 0 or word not in words:
        return False
    try:
        update_hand(hand, word)
    except (ValueError, TypeError) as e:
        return False
    return (word.lower() in words)


def play_hand(hand):

    score = 0
    while True:
        print('Current Hand: ', display_hand(hand))
        choice = input('Enter word, or a \".\" to indicate that you are finished:')

        if choice == '.':
            break

        valid = is_valid_word(WORDS_FROM_FILE, choice, hand)
        if not valid:
            print('Word is invalid')
        else:
            points = get_word_score(choice, HAND_SIZE)
            score += points
            hand = update_hand(hand, choice)
            print('\"%s\" earned %i points. Total: %i points.' % (choice, points, score))

    print('Goodbye! Total score: %i points.' % score)


def get_words(letters):
    '''Generate all posible words from hand'''
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))


def comp_choose_word(words):
    '''Choose word with maximal score '''
    word_score = 0
    choosed_word = ''
    for word in words:
        if is_valid_word(WORDS_FROM_FILE, word, hand):
            word_score_tmp = get_word_score(word, HAND_SIZE)
            # print(word_score_tmp)
            if word_score_tmp > word_score:
                word_score = word_score_tmp
                choosed_word = word
    return choosed_word


def comp_play_hand(hand):

    score = 0
    while hand:
        choosed_word = ''  # clean word before new iteration
        letters = display_hand(hand)
        print('Current Hand: ', letters)
        generated_words = list(get_words(letters))
        generated_words.sort(key=lambda s: len(s), reverse=True)
        choosed_word = comp_choose_word(generated_words)
        if len(choosed_word) == 0:
            break
        print('choosed word %s' % choosed_word)
        points = get_word_score(choosed_word, HAND_SIZE)
        score += points
        # print(hand)
        hand = update_hand(hand, choosed_word)
        print('\"%s\" earned %i points. Total: %i points.' % (choosed_word, points, score))
    print('Goodbye! Total score: %i points.' % score)

if __name__ == '__main__':

    WORDS_FROM_FILE = load_words()
    hand = {}

    while True:
        action = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if action == 'e':
            break
        elif action == 'n' or action == 'r':
            if action == 'n':
                hand = generate_hand(HAND_SIZE)
            elif action == 'r' and not hand:
                print('You have not played a hand yet. Please play a new hand first!')
                continue
                
            choose_player = input('Enter u to have yourself play, c to have the computer play:')
            if choose_player == 'u':
                play_hand(hand.copy())
            elif choose_player == 'c':
                comp_play_hand(hand.copy())
            else:
                print('Invalid command.')
        else:
            print('Invalid command.')
