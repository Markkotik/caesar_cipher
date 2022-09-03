"""Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом
Цезаря. Она должна запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо
будет преобразован в: "Фнпн Спттйя ож рпоауэ"."""

print('Здравствуйте! Это программа "Шифр Цезаря"')
print('Ответьте, на следующие вопросы:')

encryption = int(input("0 - шифровка, 1 - дешифровка"))
language = int(input("0 - английский алфавит, 1 - русский"))
step = int(input("Введите шаг шифровки"))
string = input("Введите вашу фразу")
result = ''


def encrypted_char(char, step_, encript, lang):  # функция "сдвигающая" букву

    letter = ord(char) + [step_, -step_][encript]  # вычисляет букву со сдвигом по таблице unicode + выбирает
    # направление сдвига
    if char.isupper():  # если буква заглавная
        if not [65, 1040][lang] <= letter <= [90, 1071][lang]:  # если буква не в диапазоне алфавита. 65 - 90 это
            # анг алфавит, 1040 - 1071 рус.
            letter += [26, 32][lang] * [-1, 1][encript]  # возвращаем в диапазон в зависимости от шифруем/дешифруем
    elif char.islower():
        if not [97, 1072][lang] <= letter <= [122, 1103][lang]:
            letter += [26, 32][lang] * [-1, 1][encript]

    return chr(letter)


for i in string:
    if i.isalpha():
        result += encrypted_char(i, step, encryption, language)
    else:
        result += i

print(result)
