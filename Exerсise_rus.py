"""Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо 
на 10 символов."""


def encrypted_char(char, len):  # функция "сдвигающая" букву

    letter = ord(char) + len  # вычисляет букву со сдвигом по таблице unicode
    if char.isupper():  # если символ выходит за пределы алфавита - мы его возвращаем
        if letter > 1071:
            letter -= 32
    else:
        if letter > 1103:
            letter -= 32

    return chr(letter)


s = "Блажен, кто верует, тепло ему на свете!"
s1 = ''

for i in s:
    if i.isalpha():
        s1 += encrypted_char(i, 10)
    else:
        s1 += i

print(s1)