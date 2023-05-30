x = 0
d = 100
r = 50
p = 0
while True:
    print(f'Ваше число равно{r}')
    ot = input('больше или меньше или да:')
    p += 1
    if ot == 'больше':
        x = r
        r = (x + d) // 2
    elif ot == 'меньше':
        d = r
        r = (x + d) // 2

    elif ot == 'да':
        print(f'Я угадал !')
        break
    else:
        print('вы неправильно написали пишите так "да, больше, меньше"')
    with open('pop.file', 'w', encoding='utf-8') as file:
        file.write(f'Количество попыток {p}')
