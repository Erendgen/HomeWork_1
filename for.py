"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [
        {'school_class': '4a', 'scores': [3,4,1,5,2]},
        {'school_class': '4b', 'scores': [1,1,3,4,5]},
        {'school_class': '4c', 'scores': [2,5,5,5,4]},
    ]
    scores_sum = 0
    scores_count = 0

    for i in school:
        scores_sum += sum(i['scores'])
        scores_count += len(i['scores'])
        print(f'Средняя оценка по классу {i["school_class"]} : {sum(i["scores"])/len(i["scores"])}')
      
    print(f'Средняя оценка по школе: {round(scores_sum/scores_count, 2)}')

if __name__ == "__main__":
    main()