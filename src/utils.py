from typing import Any

from src.get_top_vacancies import get_top_vacancies
from src.hh_api import HH
from src.vacancy import Vacancy
from src.work_with_json import WorkWithJson


def user_interaction() -> Any:
    print("Привет! Добро пожаловать в приложение по работе с вакансиями с сайта hh.ru.")
    print("По какому ключевому слову найти вакансии?")
    key_word = input()

    python1 = HH()
    python1.get_vacancies(key_word)
    raw_vacancies = python1.vacancies
    formated_list_json = WorkWithJson()
    formated_list_json.save_to_json(raw_vacancies)

    print(
        f"По ключевому слову '{key_word}' было найдено вакансий: {len(raw_vacancies)}"
    )

    print(
        "Вы можете отсортировать выбранные вакансии по ключевому слову в описании. Введите слово для сортировки:"
    )

    filter_word = input()

    filtered_vacancies = formated_list_json.get_data_from_json(filter_word)

    print(
        f"'{filter_word}' в описании было найдено в {len(filtered_vacancies)} вакансиях."
    )

    print("Введите, сколько вакансий вывести (будет выведен топ вакансий по зарплате):")

    top_number = int(input())

    top_vacancies = get_top_vacancies(top_number, filtered_vacancies)

    print(f"Вот топ {top_number} вакансий по зарплате:")
    vacancies = [
        Vacancy(
            vacancy["id"],
            vacancy["name"],
            vacancy["salary"],
            vacancy["url"],
            vacancy["experience"],
            vacancy["employment"],
            vacancy["description"],
        )
        for vacancy in top_vacancies
    ]

    for vacancy in vacancies:
        print(vacancy.__str__())

    print(
        "Спасибо, что обратились к этой программе! Если Вы хотите начать поиск заново - перезапустите консоль."
    )


if __name__ == "__main__":
    user_interaction()
