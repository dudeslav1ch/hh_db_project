import psycopg2
from src.DBManager import DBManager


def start_user_interaction(data):
    x = 1
    print('Доступные компании:')
    for i in data:
        print(f'№{x} - {i}')
        x += 1
    print()


def user_interaction(params):
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                manager = DBManager(cur)
                while True:
                    user_input = input('\nВыберите, что бы вы хотели сделать\n'
                                       '0 - Закрыть программу\n'
                                       '1 - Получить список всех компаний и количество вакансий у каждой компании.\n'
                                       '2 - Получить список всех вакансий с указанием названия компании, '
                                       'названия вакансии и зарплаты и ссылки на вакансию.\n'
                                       '3 - Получить среднюю зарплату по вакансиям\n'
                                       '4 - Получить список всех вакансий, '
                                       'у которых зарплата выше средней по всем вакансиям\n'
                                       '5 - Получить список всех вакансий, '
                                       'в названии которых содержатся переданные в метод слова, например "аналитик".\n'
                                       '\n'
                                       )

                    if user_input.isdigit() and 0 <= int(user_input) <= 5:
                        if user_input == '0':
                            break
                        elif user_input == '1':
                            print(manager.get_companies_and_vacancies_count())
                        elif user_input == '2':
                            print(manager.get_all_vacancies())
                        elif user_input == '3':
                            print(manager.get_avg_salary())
                        elif user_input == '4':
                            print(manager.get_vacancies_with_higher_salary())
                        elif user_input == '5':
                            user_input = input('Введите запрос: ')
                            print(manager.get_vacancies_with_keyword(user_input))
                    else:
                        print('Вводите только цифры от 0 до 5, пожалуйста')

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('Спасибо за использование. Всего хорошего!')
