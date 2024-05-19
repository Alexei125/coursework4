import pytest
from src.vacancies import Vacancy
from src.func import Functions


import pathlib
from io import StringIO


data = [{'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 900000,"to": 160000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 100000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 90000,"to": 120000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 90000,"to": 99000,"currency": "RUR"},
        "snippet": {"requirement": "Умный.","responsibility": "Красивый."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 90,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        }]

@pytest.fixture()
def vacancy():
    return Vacancy.cast_to_object_list(data)

@pytest.fixture
def for_work_with_api(monkeypatch):
    words = StringIO("2\n1\nPython\n2\nBackend SQL\n3\n150000\n4\n5\n5\n"
                          "6\n7\ntest_api_complete.json\nstop")
    monkeypatch.setattr('способен работать', words)
def test_filter_by_salary(vacancy, for_work_with_api):
    instance_sorted_class = Functions.similar_vacancies(vacancy)
    assert instance_sorted_class[0].salary == [90000, 160000]
    assert instance_sorted_class[1].salary == 100000
    assert instance_sorted_class[2].salary == [90000, 120000]
    assert instance_sorted_class[3].salary == 90