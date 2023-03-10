from random import choice

def hello():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

def bye():
    print('До новых встреч!')

def what_is_your_name():
    return input('Как тебя зовут?\n')

def hello_name(name):
    print(f"Привет, {name}")

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай', 
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

def loop():
    while True:
        input('Введи свой вопрос.\n')
        print(choice(answers))
        answer = input('Если вы хотите уйти, напишите "Хватит". Если хотите продолжить - "Продолжаем"\n')
        if answer.lower() == 'хватит':
            break

hello()
name = what_is_your_name()
hello_name(name)
loop()
bye()
