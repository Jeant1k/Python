def hello():
    print('Приветствую в своей программе по шифровке/дешифровке сообщений методом Цезаря!')

def direction():
    answer = input('Скажи, пожалуйста, ты хочешь зашифровать или расшифровать сообщение? Если ты хочешь зашифровать, напиши "зашифровать". Если расшифровать - "расшифровать"\n').strip().lower()
    while answer != 'зашифровать' and answer != 'расшифровать':
        answer = input('Вы ввели некорректные данные. Введите еще раз.\n').strip().lower()
    return answer

def language():
    answer = input('Скажи, пожалуйста, ты хочешь это сделать на русском или английском языке? Если ты хочешь на английском, напиши "английский". Если на русском - "русский"\n').strip().lower()
    while answer != 'английский' and answer != 'русский':
        answer = input('Вы ввели некорректные данные. Введите еще раз.\n').strip().lower()
    return answer

def shift():
    answer = input('Скажи, пожалуйста, какой сдвиг ты бы хотел сделать? Введи число.\n').strip().lower()
    while not answer.isdigit():
        answer = input('Вы ввели некорректные данные. Введите еще раз.\n').strip().lower()
    return int(answer)

def string():
    return input('Введите строку, которую нужно преобразовать.\n')

def ceasar(direction, language, shift, string):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    if language == 'русский':
        alphas = 32
        low_alphabet = lower_rus_alphabet
        upp_alphabet = upper_rus_alphabet
    if language == 'английский':
        alphas = 26
        low_alphabet = lower_eng_alphabet
        upp_alphabet = upper_eng_alphabet
    for i in range(len(string)):
        if string[i].isalpha():
            if direction == 'зашифровать':
                if string[i] == string[i].upper():
                    string = string[:i] + upp_alphabet[(upp_alphabet.find(string[i]) + shift) % alphas] + string[i + 1:]
                if string[i] == string[i].lower():
                    string = string[:i] + low_alphabet[(low_alphabet.find(string[i]) + shift) % alphas] + string[i + 1:]
            elif direction == 'расшифровать':
                if string[i] == string[i].upper():
                    string = string[:i] + upp_alphabet[(upp_alphabet.find(string[i]) - shift) % alphas] + string[i + 1:]
                if string[i] == string[i].lower():
                    string = string[:i] + low_alphabet[(low_alphabet.find(string[i]) - shift) % alphas] + string[i + 1:]
        else:
            continue
    return string

string = ceasar(direction(), language(), shift(), string())
print(string)
