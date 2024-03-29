"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def get_summ(num_one, num_two):
    """
    Замените pass на ваш код
    """
    try:
        num_one_int = int(num_one)
        try:
            num_two_int = int(num_two)
            return num_one_int + num_two_int        
        except ValueError:
            print('Проблема во втором аргументе.Не удалось привести к int')        
    except ValueError:
        print('Проблема в первом аргументе.Не удалось привести к int')

if __name__ == "__main__":
    print(f'get_summ(2, 2): {get_summ(2, 2)}')
    print(f'get_summ(3, "3"): {get_summ(3, "3")}')
    print(f'get_summ("4", "4"): {get_summ("4", "4")}')
    print(f'get_summ("five", 5): {get_summ("five", 5)}')
    print(f'get_summ("six", "шесть"): {get_summ("six", "шесть")}')
    print(f'get_summ("6", "шесть"): {get_summ("6", "шесть")}')
