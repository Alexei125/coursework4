from src.hh_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.func import Functions


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(Functions.request())

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    Functions.work_with_user(vacancies_list)


if __name__ == "__main__":
    main()