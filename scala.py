from math import factorial


def round_to_half(i):
    i = str(round(i, 1))
    first_character = int(float(i))
    last_character = i[-1]
    if int(last_character) >= 5:
        last_character = 5
    else:
        last_character = 0
    return f'{first_character}.{last_character}'


def get_scale(pkt):
    final = []
    not_final = []
    arr = [['cel', pkt, pkt], ['bdb', pkt * 88 / 100, pkt * 99 / 100], ['db', pkt * 72 / 100, pkt * 87 / 100],
           ['dst', pkt * 56 / 100, pkt * 71 / 100], ['dop', pkt * 41 / 100, pkt * 55 / 100],
           ['ndst', pkt * 0 / 100, pkt * 40 / 100]]
    for i in arr:
        not_final.append([i[0], round_to_half(i[1]), round_to_half(i[2])])
        final.append(not_final)
        not_final = []
    return final


def pascal_tr(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")

        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print('\n')


def pascal_another_method(a):
    lst = [1]
    for i in range(a):
        print(lst)
        mylist = []
        mylist.append(lst[0])
        for i in range(len(lst) - 1):
            mylist.append(lst[i] + lst[i + 1])
        mylist.append(lst[-1])
        lst = mylist
    return lst


'''
ocena celująca – 100%;
ocena bardzo dobra – od 88% do 99%;
ocena dobra – od 72% do 87%;
ocena dostateczna – od 56% do 71%;
ocena dopuszczająca – od 41% do 55%;
ocena niedostateczna – 0% do 40%;
'''
