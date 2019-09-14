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
    scores_sum_4a = 0
    scores_count_4a = 0
    scores_sum_4b = 0
    scores_count_4b = 0
    scores_sum_4c = 0
    scores_count_4c = 0
    
    
    for i in school:
        scores_sum += sum(i['scores'])
        scores_count += len(i['scores'])
        if i['school_class'] == '4a':
            scores_sum_4a += sum(i['scores'])
            scores_count_4a += len(i['scores'])
        if i['school_class'] == '4b':
            scores_sum_4b += sum(i['scores'])
            scores_count_4b += len(i['scores'])
        if i['school_class'] == '4c':
            scores_sum_4c += sum(i['scores'])
            scores_count_4c += len(i['scores'])        
            


    print(f'Средняя оценка по школе: {round(scores_sum/scores_count, 2)}')
    print(f'Средняя оценка по классу "4a": {round(scores_sum_4a/scores_count_4a, 2)}')
    print(f'Средняя оценка по классу "4b": {round(scores_sum_4b/scores_count_4b, 2)}')
    print(f'Средняя оценка по классу "4c": {round(scores_sum_4c/scores_count_4c, 2)}')  
        
if __name__ == "__main__":
    main()