def number(lst, num=1000):
    search = list([abs(i - num), i] for i in lst)
    search.sort()
    search2 = list()
    for i in search:
        search2.append(i[-1])
    return num, search2


# print(number([12, 354, 65, 79]))
def index(sectionc):
    while True:
        try:
            print('Введите exit что бы выйти!')
            index = input('Введите индекс:')
            if index == 'exit':
                print('Программа остановлена!')
                break
            print(sectionc[int(index)])
        except ValueError:
            print('Пишите только цифры!')
        except IndexError:
            print('Введите индекс от 0 до 4')


index([True, 12, 'red', 45, 90])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = lambda i: i % 2 == 0
filtr = filter(num, numbers)
# print("", list(filtr))

mapu = ['lte', 'map', 'audi', 'bwm']
up_str = list(map(str.upper, mapu))
# print(up_str)
