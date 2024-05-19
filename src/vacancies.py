class Vacancy:
    def __init__(self, name, url, salary, currency, requirement, responsibility):
        self.name = name    #название вакансии
        self.url = url    #ссылка на вакансию
        self.salary = self.get_product_price(salary)    #зарплата
        self.salary_for_filtering = self.filter_list()     #зарплата для фильтрации (атрибут используется только для фильтрации!!!)
        self.currency = self.currency(currency)    #валюта
        self.requirement = self.check_source_info(requirement)    #требования
        self.responsibility = self.check_source_info(responsibility)    #обязанности


    @staticmethod
    def check_source_info(value):
        if value:
            return value
        return 'информация не была найдена'

    @staticmethod
    def get_product_price(salary):
        """
        возвращает зарплату в формате 100000 или [100000, 150000]
        """

        if isinstance(salary, list) or isinstance(salary, int):
            return salary
        else:
            salary_from = salary.get('from', None)
            salary_to = salary.get('to', None)
            if salary_to is None and salary_from is None:
                return 0
            elif salary_to is None:
                return salary_from
            elif salary_from is None:
                return salary_to
            else:
                return [salary_from, salary_to]

    @staticmethod
    def currency(currency):
        """
        возвращает валюту
        """
        if isinstance(currency, str):
            return currency  # валюта
        return 'валюта не указана'

    def filter_list(self):
        """
        функция высчитывает среднюю зп из вакансий у который указан диапазон зарплат для фильтрации по убыванию
        атрибут используется только для фильтрации!!!
        :self.salary: принимает: 100000 - 200000
        :return: 150000
        """
        if isinstance(self.salary, list):
            return (self.salary[0] + self.salary[-1]) / 2
        return self.salary


    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        returned_list = []
        for vacancy in hh_vacancies:
            # print(vacancy)
            name = vacancy['name']  # название вакансии
            url = vacancy['apply_alternate_url']  # ссылка на вакансию
            if vacancy["salary"] is None:
                salary = 0
                currency = "валюта не указана"
            else:
                salary = vacancy["salary"]  # зарплата
                currency = vacancy["salary"]["currency"]    #валюта
            requirement = vacancy['snippet']['requirement']  # краткое описани
            responsibility = vacancy['snippet']['responsibility']  # краткое описани
            returned_list.append(cls(name, url, salary, currency, requirement, responsibility))
        return returned_list

    @classmethod
    def vacancies_from_file(cls, vacancies):
        returned_list = []
        for vacancy in vacancies:
            # print(vacancy)
            name = vacancy['name']  # название вакансии
            url = vacancy['url']  # ссылка на вакансию
            salary = vacancy['salary']  # зарплата
            currency = vacancy["currency"]  # валюта
            requirement = vacancy['requirement']  # краткое описани
            responsibility = vacancy['responsibility']  # краткое описани
            returned_list.append(cls(name, url, salary, currency, requirement, responsibility))
        return returned_list


    def __gt__(self, other):  # – для оператора больше >
        if type(other) is type(self):
            return self.salary_for_filtering > other.salary_for_filtering
        return self.salary_for_filtering > other

    def __str__(self):
        if isinstance(self.salary, list):
            return (f'Вакансия: {self.name}\n'
                    f'Зарплата: {' - '.join(list(map(str, self.salary)))} {self.currency}\n'
                    f'Требования: {self.requirement.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                    f'Обязанности: {self.responsibility.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                    f'Ссылка на вакансию: {self.url}\n'
                    f'-------------------------------------------------------------------------------')
        else:
            return (f'Вакансия: {self.name}\n'
                    f'Зарплата: {self.salary} {self.currency}\n'
                    f'Требования: {self.requirement}\n'
                    f'Обязанности: {self.responsibility}\n'
                    f'Ссылка на вакансию: {self.url}\n'
                    f'-------------------------------------------------------------------------------')


