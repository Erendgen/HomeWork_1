def main(str1, str2):        
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3
        else:
            return '"В задаче не описано что возвращать"'
    else:
        return 0

str1 = 'QWE'
str2 = 'QWE'
print('Строки одинаковые, печатаем ' + str(main(str1, str2)))
str1 = 'QWE34'
str2 = 'QWE'
print('Строки разные и первая строка длиннее, печатаем ' + str(main(str1, str2)))
str1 = 'QWE34'
str2 = 'learn'
print('Строки разные и вторая строка "learn", печатаем ' + str(main(str1, str2)))
str1 = 1
str2 = 'asdasd'
print('Один из аргументов функции не строка, печатаем ' + str(main(str1, str2)))
str1 = 'sad'
str2 = 'asdasd'
print('Не описанный случай в задаче: первая строка короче второй, печатаем ' + str(main(str1, str2)))