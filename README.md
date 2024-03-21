# Парсер вакансий HeadHunter'а
Выводит информацию о вакансиях HH по запросу пользователя, используя SQL-запросы
## **Структура проекта:**

### **src:**

* [DBCreation.py](src/DBCreation.py) - класс для создания бд и таблиц + заполнение таблиц
* [DBManager.py](src/DBManager.py) - класс с SQL-запросами
* [GetApiHh.py](src/GetApiHh.py) - класс для вывода вакансий и работодателей из HH
* [utils.py](src/utils.py) - функции для работы с пользователем


### root:

* [config](config.py) - конфиг для подключения к SQL
* [main](main.py):
*   [sql_setup()](main.py) - создает БД(удаляет старую при необходимости)
*   [main()](main.py) - взаимодействие с пользователем
* [database.ini](database.ini) - заглушка, написать свои данные
