"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dict_x = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты сегодня ел?": "Нет"}
def ask_user():
    """
    Замените pass на ваш код
    """
    try:        
        while True:
            question = input('Введите вопрос: ')    
            if dict_x[question]:
                print(dict_x[question])
    except KeyError:
        print('Нет значения в словаре')
    except KeyboardInterrupt:
        print('Пока')

if __name__ == "__main__":
    ask_user()