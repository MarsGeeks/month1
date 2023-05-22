def even_odd(number):
    if number % 2 == 0:
        print('Четное число')
        return number
    else:
        print('Нечетное число')
        return False


even_odd(int(input('Введите число:')))


def provopisanie(sentence):
    if sentence[0].isupper() and sentence[-1] == '.':
        return sentence
    else:
        return 'Предложение должно начинаться с Большой буквы и заканчиваться точкой'


def list_avrg(*lst):
    return int(sum(lst) // len(lst))


def nearest_number(seq, number=0):
    nearest_num = seq[0]
    for i in seq:
        if abs(i - number) < abs(number - nearest_num):
            nearest_num = i
    return nearest_num
