import json

import pytest

from src.work_with_json import WorkWithJson


@pytest.fixture
def vacancies_list():
    return [
        {
            "id": "105338726",
            "premium": False,
            "name": "Junior Python developer",
            "department": None,
            "alternate_url": "https://hh.ru/vacancy/105338726",
            "salary": {"from": None, "to": 800, "currency": "USD", "gross": True},
            "snippet": {
                "requirement": "Знание <highlighttext>Python</highlighttext> инструментов тестирования (Selenium, PyTest). ",
                "responsibility": "Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации тестирования блокчейн и инфраструктурных проектов.",
            },
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
        }
    ]


# "data/vacancies.json"


def test_save_to_json(vacancies_list):
    result = WorkWithJson()
    result.save_to_json(vacancies_list, "data/vacancies.json")
    with open("data/vacancies.json", encoding="utf-8") as f:
        result_json = json.load(f)
    assert result_json == [
        {
            "id": "105338726",
            "name": "Junior Python developer",
            "salary": {"from": None, "to": 800, "currency": "USD", "gross": True},
            "url": "https://hh.ru/vacancy/105338726",
            "experience": "От 1 года до 3 лет",
            "employment": "Полная занятость",
            "description": "Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации тестирования блокчейн и инфраструктурных проектов.",
        }
    ]


def test_delete_from_json():
    original = [
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
        {"id": 5},
        {"id": 6},
        {"id": 7},
        {"id": 8},
        {"id": 9},
        {"id": 10},
    ]
    with open("data/vac4.json", "w", encoding="utf-8") as f:
        json.dump(original, f)
    result1 = WorkWithJson()
    result1.delete_from_json([2, 3, 4, 7, 9], "data/vac4.json")
    with open("data/vac4.json", encoding="utf-8") as f:
        result1_json = json.load(f)
    assert result1_json == [{"id": 1}, {"id": 5}, {"id": 6}, {"id": 8}, {"id": 10}]


def test_get_data_from_json():
    original1 = [
        {"description": "a word"},
        {"description": "nothing to find"},
        {"description": "word again"},
        {"description": "one more word"},
        {"description": "and again nothing"},
    ]
    with open("data/vac3.json", "w", encoding="utf-8") as f:
        json.dump(original1, f, ensure_ascii=False)
    result2 = WorkWithJson()
    result2.get_data_from_json("word", "data/vac3.json")
    with open("data/vac3.json", encoding="utf-8") as f:
        result1_json = json.load(f)
    assert result1_json == [
        {"description": "a word"},
        {"description": "word again"},
        {"description": "one more word"},
    ]
