from random import choice
import os

def get_word_list():
    f = open('words.txt', 'r')
    word_list = []
    for line in f:
        word = ''
        for i in line:
            if i == ';':
                break
            word += i
        word_list.append(word)
    return word_list

def get_word(word_list):
    return choice(word_list).upper()

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return print(stages[tries])

def letter_word_input():
    letter_word = input('Введите букву или слово: ').strip()
    while not letter_word.isalpha():
        letter_word = input('Вы ввели некоррктные данные. Введите букву или слово: ').strip()
    return letter_word.upper()
    
def print_word_completion(word_completion):
    print('Ваше слово:', word_completion)

def lets_play():
    print('Давайте играть в угадайку!')

def find_all_indexes(word, letter):
    res, count = [], 0
    for i in word:
        if i == letter:
            res.append(count)
        count += 1
    return res

def display(tries, word_completion):
    lets_play()
    display_hangman(tries)
    print_word_completion(word_completion)

def play(word):
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    while True:
        os.system('clear')
        display(tries, word_completion)
        if tries == 0:
            print('Вы проиграли. Было загадано слово:', word)
            break
        if word_completion.isalpha():
            print('Вы угадали слово!')
            break
        letter_word = letter_word_input()
        if len(letter_word) == 1:
            while letter_word in guessed_letters:
                print('Вы уже называли эту букву. Введите другую.')
                letter_word = letter_word_input()
            if letter_word in word:
                guessed_letters.append(letter_word)
                indexes = find_all_indexes(word, letter_word)
                for i in indexes:
                    word_completion = word_completion[:i] + letter_word + word_completion[i + 1:]
            else:
                tries -= 1
                guessed_letters.append(letter_word)
        else:
            while letter_word in guessed_words:
                print('Вы уже называли это слово. Введите другое.')
                letter_word = letter_word_input()
            if letter_word == word:
                print('Вы угадали слово!')
                break
            else:
                tries -= 1
                guessed_words.append(letter_word)      

def break_the_game():
    answer = input('Желаете сыграть еще раз? Если да, напишите "да". Если нет - "нет"\n')
    while answer != 'да' and answer != 'нет':
        answer = input('Вы ввели некорректные данные. Введите еще раз.\n')
    if answer == 'нет':
        return True
    return False
    
word_list = get_word_list()
while True:
    word = get_word(word_list)
    play(word)
    if break_the_game():
        break
