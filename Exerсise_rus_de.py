"""Текст "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг." был получен в результате шифрования алгоритмом
Цезаря с сдвигом вправо на 7 символов. Расшифруйте данный текст."""


def encrypted_char(char, len):  # функция "сдвигающая" букву

    letter = ord(char) - len  # вычисляет букву со сдвигом по таблице unicode
    if char.isupper():  # если символ выходит за пределы алфавита - мы его возвращаем
        if letter < 1040:
            letter += 32
    else:
        if letter < 1072:
            letter += 32

    return chr(letter)


s = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
s1 = ''

for i in s:
    if i.isalpha():
        s1 += encrypted_char(i, 7)
    else:
        s1 += i

print(s1)