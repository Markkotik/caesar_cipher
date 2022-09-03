'''Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования
алгоритмом Цезаря с сдвигом вправо на n символов. Расшифруйте данный текст.'''


def encrypted_char(char, len):  # функция "сдвигающая" букву

    letter = ord(char) - len  # вычисляет букву со сдвигом по таблице unicode
    if char.isupper():  # если символ выходит за пределы англ. алфавита - мы его возвращаем
        if letter < 65:
            letter += 26
    else:
        if letter < 97:
            letter += 26

    return chr(letter)


s = "Hawnj pk swhg xabkna ukq nqj."
s1 = ''

for j in range(1, 26):
    for i in s:
        if i.isalpha():
            s1 += encrypted_char(i, j)
        else:
            s1 += i

    print(s1)
    s1 = ''
