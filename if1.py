def main():
    age = input('Введите возраст: ')
    if age.isdigit():
        if int(age) >= 3 and int(age) < 7:
            occupation = 'Детский сад'
        elif int(age) >= 7 and int(age) < 18:
            occupation = 'Школа'
        elif int(age) >=18 and int(age) < 23:
            occupation = 'ВУЗ'
        elif int(age) >=23 and int(age) < 65:
            occupation =  'Работа'
        else:
            occupation = 'Занятие не определено'
        print(occupation)
    else:
        print('Введено не целое неотрицательное число')
if __name__ == "__main__":    
    main()
    