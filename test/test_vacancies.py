import pytest
from src.vacancies import Vacancy

data = [{'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 30000,"to": 44000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        }]

@pytest.fixture()
def vacancy():
    return Vacancy.cast_to_object_list(data)


def test_init_vacancy(vacancy):
    assert vacancy[0].name == 'яндекс'
    assert vacancy[0].url == 'ссылка'
    assert vacancy[0].salary == [30000, 44000]
    assert vacancy[0].currency == 'RUR'
    assert vacancy[0].requirement == 'Способен работать в команде.'
    assert vacancy[0].responsibility == 'Работать с клиентами или партнерами.'

data_2 = [{
        "name": "Стажер-разработчик Python",
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=94354526",
        "salary": [
            100000,
            150000
        ],
        "salary_for_filtering": 125000.0,
        "currency": "RUR",
        "requirement": "Способен работать в команде.",
        "responsibility": "Работать с клиентами или партнерами."
    }]

@pytest.fixture()
def vacancy_2():
    return Vacancy.vacancies_from_file(data_2)


def test_init_vacancy_2(vacancy_2):
    assert vacancy_2[0].name == 'Стажер-разработчик Python'
    assert vacancy_2[0].url == 'https://hh.ru/applicant/vacancy_response?vacancyId=94354526'
    assert vacancy_2[0].salary == [100000, 150000]
    assert vacancy_2[0].currency == 'RUR'
    assert vacancy_2[0].requirement == 'Способен работать в команде.'
    assert vacancy_2[0].responsibility == 'Работать с клиентами или партнерами.'