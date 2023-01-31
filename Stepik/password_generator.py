from random import choice

def hello():
    print('Приветствую в программе, генирирующей пароли!')

def password_number():
    num = input('Введите количество паролей, которые вы хотели бы сгенирировать.\n').strip()
    while not num.isdigit():
        num = input('Введите корректные данные.\n').strip()
    return int(num)

def password_length():
    len = input('Введите длину паролей, которые вы хотели бы сгенирировать.\n').strip()
    while not len.isdigit():
        len = input('Введите корректные данные.\n').strip()
    return int(len)

def include_numbers():
    answer = input('Хотите ли вы, чтобы в вашем пароле были цифры? Напишите "да" или "нет"\n').strip()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректные данные.\n').strip()
    if answer == 'нет':
        return False
    return True

def include_capital_letters():
    answer = input('Хотите ли вы, чтобы в вашем пароле были прописные буквы? Напишите "да" или "нет"\n').strip()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректные данные.\n').strip()
    if answer == 'нет':
        return False
    return True

def include_lower_letters():
    answer = input('Хотите ли вы, чтобы в вашем пароле были строчные буквы? Напишите "да" или "нет"\n').strip()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректные данные.\n').strip()
    if answer == 'нет':
        return False
    return True

def include_special_symbols():
    answer = input('Хотите ли вы, чтобы в вашем пароле были специальные символы? Напишите "да" или "нет"\n').strip()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректные данные.\n').strip()
    if answer == 'нет':
        return False
    return True

def exclude_ambigious_characters():
    answer = input('Хотите ли вы, чтобы в вашем пароле были исключены неоднозначные символы il1Lo0O? Напишите "да" или "нет"\n').strip()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректные данные.\n').strip()
    if answer == 'нет':
        return False
    return True

def generate_password(password_number, password_length, chars):
    list_of_passwords = []
    for i in range(password_number):
        password = ''
        for _ in range(password_length):
            password += choice(chars)
        list_of_passwords.append(password)
    return list_of_passwords

def print_passwords(passwords):
    for i in passwords:
        print(i)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

hello()
password_number = password_number()
password_length = password_length()
include_numbers = include_numbers()
include_capital_letters = include_capital_letters()
include_lower_letters = include_lower_letters()
include_special_symbols = include_special_symbols()
exclude_ambigious_characters = exclude_ambigious_characters()

chars = ''

if include_numbers:
    chars += digits
if include_capital_letters:
    chars += uppercase_letters
if include_lower_letters:
    chars += lowercase_letters
if include_special_symbols:
    chars += punctuation
if exclude_ambigious_characters:
    chars = ''.join(i for i in chars if not i in 'il1Lo0O')

passwords = generate_password(password_number, password_length, chars)
print_passwords(passwords)
