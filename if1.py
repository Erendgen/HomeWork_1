try:
    age = int(input('Введите возраст: '))
    def main(age):
        if age >= 3 and age < 7:
            occupation = 'Детский сад'
        elif age >= 7 and age < 18:
            occupation = 'Школа'
        elif age >=18 and age < 23:
            occupation = 'ВУЗ'
        elif age >=23 and age < 65:
            occupation =  'Работа'
        else:
            occupation = 'Занятие не определено'
        return occupation
    x = main(age)
    print(x)
except ValueError:
    print('Введено не целое число')