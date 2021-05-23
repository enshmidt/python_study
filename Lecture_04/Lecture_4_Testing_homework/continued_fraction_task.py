def continued_fraction(a, b):
    """
    1. Берем два числа
    2. Делим, выделяем целое число
    3. Получаем остаток от деления
    4. Переворачиваем местами знаменатель и остаток от деления
    5. повторяем п. 2-4
    6. до тех пор, пока остаток от деления не будет равен 0
    """
    num, denum = a, b
    res = []
    while denum != 0:
        whole = num // denum
        res.append(whole)
        num, denum = denum, num % denum
    return res
