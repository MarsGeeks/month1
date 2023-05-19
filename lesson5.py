countries = {
    'kg': {'red', 'yellow'},
    'kz': {'blue', 'yellow'},
    'ru': {'blue', 'white', 'red'},
    'uk': {'yellow', 'blue'}
}
while True:
    print('чтобы выйти напишите q')
    user_colors = input('Введите свет:').split()
    p = 0
    for name, colors in countries.items():
        sum = 0
        for i in user_colors:
            if i in colors:
                sum += 1
        if sum == len(user_colors):
            print(name)
            p += 1
    if user_colors[0] == 'q':
        print('Вы вышли с программы!!')
        break

    elif p == 0:
        print('с таким светом страны нету')




