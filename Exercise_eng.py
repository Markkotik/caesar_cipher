'''Зашифруйте текст "To be, or not to be, that is the question!" алгоритмом Цезаря с сдвигом
вправо на 1717 символов.'''


def encrypted_char(char, len):  # функция "сдвигающая" букву

    letter = ord(char) + len  # вычисляет букву со сдвигом по таблице unicode
    if char.isupper():  # если символ выходит за пределы англ. алфавита - мы его возвращаем
        if letter > 90:
            letter -= 26
    else:
        if letter > 122:
            letter -= 26

    return chr(letter)


s = "To be, or not to be, that is the question!"
s1 = ''

for i in s:
    if i.isalpha():
        s1 += encrypted_char(i, 17)
    else:
        s1 += i

print(s1)