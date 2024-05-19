from src.utils import filter_by_salary, sorted_by_salary
import os
from config import ROOT_DIR
from src.j_file import JSONWorker


class Functions:

    @staticmethod

    def request():
        """
        выводит поисковый запрос для запроса вакансий из hh.ru
        """
        return input('Введите поисковый запрос для поска вакансий: ')

    @staticmethod
    def top_vacancies(vacancies):
        """
        выдает топ N вакансий по зарплате
        """
        num = int(input('Какое количчество вакансий вам выдать? '))
        sorted_vacancies = sorted_by_salary(vacancies)
        for i in sorted_vacancies[0: num]:
            print(i)

    @staticmethod
    def similar_vacancies(vacancies):
        """
        получить вакансии с ключевым словом в описании
        """
        words = input("введите ключевые слова через пробел: ").split()
        reserve_list_vacancies = vacancies
        for word in words:
            list_vacancies = []
            for v in vacancies:
                if word.lower() in v.requirement.lower() or word.lower() in v.responsibility.lower():
                    list_vacancies.append(v)
            if len(list_vacancies) == 0:
                print("Вакансии с такими ключевыми словами не найдены")
                return reserve_list_vacancies
            else:
                vacancies = list_vacancies
        return vacancies

    @staticmethod
    def work_with_user(vacancies_list):
        while True:
            print('Кнопки управления:\n'
                  '1 - вывести вакансии в терминал\n'
                  '2 - отфильтровать вакансии по ключевым словам\n'
                  '3 - отфильтровать вакансии по З/П\n'
                  '4 - сортировать вакансии по убыванию З/П\n'
                  '5 - отсортировать топ N вакансий\n'
                  '6 - сохранить информацию о вакансиях в файл\n'
                  '7 - считатать данные из файла\n'
                  '8 - удалить все данные в файле\n'
                  '9 - удалить вакансии из файла не соответствующие выбранной зарплате\n'
                  '"stop" или "стоп" закончить работу\n')
            answer = input()
            if answer == "стоп" or answer == "stop":
                break
            try:
                answer = int(answer)
                if 1 <= answer <= 9:  # печатает вакансии в терминал
                    if answer == 1:
                        for i in vacancies_list:
                            print(i)

                    elif answer == 2:  # фильтрует вакансии по ключевым словам
                        vacancies_list = Functions.similar_vacancies(vacancies_list)

                    elif answer == 3:  # фильтрует вакансии по з/п
                        vacancies_list = filter_by_salary(vacancies_list)

                    elif answer == 4:  # сортирует вакансии по убыванию З/П
                        vacancies_list = sorted_by_salary(vacancies_list)
                        print('\nВакансии отсортированы\n')

                    elif answer == 5:  # отсортирует топ N вакансий
                        Functions.top_vacancies(vacancies_list)

                    elif answer == 6:  # сохраняет информацию о вакансиях в файл
                        file_name = input('Введите название файла для сохранения данных: (Пример: file )')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        json_saver.write_vacancies(vacancies_list)

                    elif answer == 7:  # считатываает данные из файла
                        file_name = input('Введите название файла для считывания данные из файла: (Пример: file )')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        vacancies_list = json_saver.read_vacancies()

                    elif answer == 8:  # удаляет информацию о вакансиях из файла
                        file_name = input('Введите название файла для удаления данных: (Пример: file )')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        json_saver.delete_vacancies()

                    elif answer == 9:  # считатываает данные из файла
                        file_name = input(
                            'Введите название файла для удаления вакансий не соответствующих выбранной зарплате: (Пример: file )')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        vacancies_list = json_saver.delete_salary_vacancies()

                else:
                    print(f"Введите цифру от 1 до 9\n")

            except ValueError:
                print(f"Введите цифру от 1 до 9\n")