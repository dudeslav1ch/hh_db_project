import requests


class GetApiHh:
    def __init__(self, employers_dict):
        self.employer_info: list = []
        self.employers_dict: dict = employers_dict
        self.url: str = f'https://api.hh.ru/vacancies/'

    def get_employer_info(self, employer_id):
        """
        Выводит информацию из HH о заказчике.
        """
        params = {
            "page": 1,
            "per_page": 100,
            "employer_id": employer_id,
            "only_with_salary": True,
            "area": 113,
            "only_with_vacancies": True
        }
        return requests.get(self.url, params=params).json()['items']

    def get_vacancies(self):
        """
        Создает список вакансий.
        """
        vacancies_list = []
        for employer in self.employers_dict:
            emp_vacancies = self.get_employer_info(self.employers_dict[employer])
            for vacancy in emp_vacancies:  # salary_from может быть равен 0
                if vacancy['salary']['from'] is None:
                    salary = 0
                else:
                    salary = vacancy['salary']['from']
                vacancies_list.append(
                    {'url': vacancy['alternate_url'], 'salary': salary,
                     'vacancy_name': vacancy['name'], 'employer': employer})
        return vacancies_list
