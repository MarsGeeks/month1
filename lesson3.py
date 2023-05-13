vse_gls = 'aeiouyeауоыиэяюе'
while True:
    kol = 0
    gls = 0
    sgls = 0
    word = input('Введите слово:')

    if word == 'break':
        print('программа останвлено!!')
        break

    for i in word:
        if i.isalpha():
            kol += 1
            if i in vse_gls:
                gls += 1
            else:
                sgls += 1
    print(f'Слово: {word} \nКличество букв: {kol}\nКоличество гласных букв: {gls}\nКоличество согласных букв: {sgls}')
    gls_prosent = round((gls * 100) / kol, 2)
    sgls_prosent = round((sgls * 100) / kol, 2)
    print(f'Гласные: {gls_prosent}%\nСогласные: {sgls_prosent}%')
