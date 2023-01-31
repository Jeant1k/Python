from random import randint
import PySimpleGUI as sg

def is_valid(str, right_boarder):
    if str.isdigit():
        if 1 <= int(str) <= right_boarder:
            return True
    return False

def get_right_boarder():
    sg.popup('Добро пожаловать в числовую угадайку! Попробуйте угадать какое число загадал компьютер.')
    layout = [[sg.Text('Вы будете угадывать числа от 1 до n. Для того чтобы начать, введите n: ')],
          [sg.Input()],
          [sg.OK('Ввод')]]
    window = sg.Window('   Угадайка', layout)
    event, values = window.read()
    right_boarder = values[0]
    while not right_boarder.isdigit() or int(right_boarder) < 1:
        sg.popup('Вы ввели некорректные данные. Попробуйте еще раз.')
        event, values = window.read()
        right_boarder = values[0]
    window.close()
    return int(right_boarder)

def loop():
    attempt_count, right_boarder = 0, get_right_boarder()
    num = randint(1, right_boarder)
    
    layout = [[sg.Text('Как вы думаете какое число загадал компьютер? Попытайте удачу! Введите ваше число.')],
          [sg.Input()],
          [sg.OK('Ввод')]]

    window = sg.Window('   Угадайка', layout)

    while True:
        attempt_count += 1
        event, values = window.read()
        answer_num = values[0]
        while not is_valid(answer_num, right_boarder):
            sg.popup('Вы ввели некорректные данные. Попробуйте еще раз.')
            event, values = window.read()
            answer_num = values[0]
        if int(answer_num) < num:
            sg.popup('Ваше число меньше загаданного, попробуйте еще разок.')
        elif int(answer_num) > num:
            sg.popup('Ваше число больше загаданного, попробуйте еще разок.')
        else:
            sg.popup(f'Вы угадали число за {attempt_count} раз!')
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()

def new_try():
    play_again_answer = sg.popup_yes_no('Хотите ли вы сыграть еще раз?')
    if play_again_answer == 'No':
        return False
    return True

sg.theme('Dark Blue 4')

play_again = True

while play_again:
    loop()
    play_again = new_try()

sg.popup('Спасибо, что играли в числовую угадайку! Еще увидимся...')
