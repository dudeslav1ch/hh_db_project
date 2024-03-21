import psycopg2


class DBCreation:

    def __init__(self, params):
        self.params = params

    def create_database(self, database_name: str):
        """
        Создаёт базы данных SQL.
        """
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f'DROP DATABASE IF EXISTS {database_name}')
        cur.execute(f'CREATE DATABASE {database_name}')

        cur.close()
        conn.close()

    def create_tables(self, database_name: str):
        """
        Создаёт таблицы employers и vacancies в базе данных.
        """
        conn = psycopg2.connect(dbname=database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE employers (
                company_id int primary key,
                employer_name varchar unique not null,
                foreign key(employer_name) references employers(employer_name)
                )
                """)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE vacancies (
                    vacancy_id serial primary key,
                    vacancy_name text not null,
                    salary int,
                    employer_name text not null,
                    vacancy_url varchar not null
                    )
                    """)

        conn.commit()
        conn.close()

    def employers_to_db(self, database_name, emp_dict):
        """
        Сохраняет работодателей в БД
        """
        with psycopg2.connect(dbname=database_name, **self.params) as conn:
            with conn.cursor() as cur:
                for employer in emp_dict:
                    cur.execute(
                        f"INSERT INTO employers values ('{int(emp_dict[employer])}', '{employer}')")

        conn.commit()
        conn.close()

    def vacancies_to_db(self, database_name, vacancies):
        """
        Сохраняет вакансии в БД
        """
        with psycopg2.connect(dbname=database_name, **self.params) as conn:
            with conn.cursor() as cur:
                for vacancy in vacancies:
                    cur.execute(
                        f"INSERT INTO vacancies(vacancy_name, salary, employer_name, vacancy_url) values "
                        f"('{vacancy['vacancy_name']}', '{int(vacancy['salary'])}', "
                        f"'{vacancy['employer']}', '{vacancy['url']}')")
        conn.commit()
        conn.close()
