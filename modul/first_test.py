def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    l = []
    s = ''
    for i in range(number):
        l.append("bulochka")
    s = ''.join(str(n) for n in l)
    return s


def my_sum(list_of_numbers):
    """Function receives a list with integer numbers,
        should return its sum as an integer. Do not use built in summarize functions.
        :param list

        Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
        Не использовать встроенные функции суммирования.

        """
    summ1 = 0
    for i in list_of_numbers:
        summ1 += int(i)
    return summ1



def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    l = []
    s = ''
    l2 = []
    t = ''
    k = ''
    for string in string:
        l.append(string.split())
    m = []
    for i in l:
        k = ''
        for word in i:
            if len(word) <= 6:
                m.append(word)
            elif len(word) > 6:
                s = ((word[:6]) + '*')
                m.append(s)
                k = ' '.join(str(x) for x in m)
        w = '\n'.join(k)
    t = ''.join(w)
    return k

# выводит все в одну строку... 

def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    count = 0
    for i in words:
        if (len(i) >= 2) and (i[:1]) == (i[-1]):
            count = count + 1
    return count

