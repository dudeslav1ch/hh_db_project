from src.GetApiHh import GetApiHh
from config import config
from src.DBCreation import DBCreation
from src.utils import start_user_interaction, user_interaction

employers_dict = {'Яндекс': "1740",
                  'epam': "29740",
                  'Sber': "3529",
                  'Whoosh': "3536822",
                  'Банк ВТБ (ПАО)': "1440683",
                  'RuTube': "78638",
                  'Cian': "1429999",
                  'RosNeft': "6596",
                  'Gazprom': "2159482",
                  'SeverStal': "6041"}
params = config()


def sql_setup():
    api_connect = GetApiHh(employers_dict)
    vacancies = api_connect.get_vacancies()

    db_setup = DBCreation(params)
    db_setup.create_database('hh_api')
    db_setup.create_tables('hh_api')
    db_setup.employers_to_db('hh_api', employers_dict)
    db_setup.vacancies_to_db('hh_api', vacancies)


def main():
    params.update({'dbname': 'hh_api'})

    start_user_interaction(employers_dict)
    user_interaction(params)


if __name__ == "__main__":
    sql_setup()
    main()
