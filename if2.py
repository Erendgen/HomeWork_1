def main(str1, str2):        
    try: 
        float(str1) #пытаемся привести введенное значение к числу
        float(str2) #пытаемся привести введенное значение к числу        
    except ValueError:
        if str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3
        else:
            return 'Обе переменные строки, но не попадают под условия задачи'
    else:
        return 0
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
print(main(str1, str2))