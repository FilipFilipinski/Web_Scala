from math import factorial


def get_scale(pkt):
    final = []
    arr = [['cel', pkt, pkt], ['bdb', pkt * 88 / 100, pkt * 99 / 100], ['db', pkt * 72 / 100, pkt * 87 / 100],
           ['dst', pkt * 56 / 100, pkt * 71 / 100], ['dop', pkt * 41 / 100, pkt * 55 / 100],
           ['ndst', pkt * 0 / 100, pkt * 40 / 100]]
    for i in arr:
        final.append([i[0], round(i[1], 1), round(i[2], 1)])
    return final


def pascal_tr(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")

        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print('\n')


'''
ocena celująca – 100%;
ocena bardzo dobra – od 88% do 99%;
ocena dobra – od 72% do 87%;
ocena dostateczna – od 56% do 71%;
ocena dopuszczająca – od 41% do 55%;
ocena niedostateczna – 0% do 40%;
'''
