import json
from typing import List

from src.hh_api import HH
from src.work_with_files import WorkWithFiles


class WorkWithJson(WorkWithFiles):
    """Класс для работы с json-файлами: для записи, получения данных и удаления информации из json-файла"""

    def __init__(self, file_name="data/vac1.json") -> None:
        self.__file_name = file_name

    def save_to_json(self, new_vac_list: List) -> None:
        """Метод добавляет новые ваканчии в файл .json"""
        with open(self.__file_name, encoding="utf-8") as f:
            original_json = json.load(f)
        id_list = []
        for item in original_json:
            id_list.append(item["id"])
        for dict_item in new_vac_list:
            if dict_item["id"] not in id_list:
                temp_dict = {}
                temp_dict["id"] = dict_item["id"]
                temp_dict["name"] = dict_item["name"]
                temp_dict["salary"] = dict_item["salary"]
                temp_dict["url"] = dict_item["alternate_url"]
                temp_dict["experience"] = dict_item["experience"]["name"]
                temp_dict["employment"] = dict_item["employment"]["name"]
                temp_dict["description"] = dict_item["snippet"]["responsibility"]
                original_json.append(temp_dict)
        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(original_json, f, ensure_ascii=False, indent=4)

    def get_data_from_json(self, key_word: str) -> None:
        """Метод ищет вакансии, в описании которых содержится ключевое слово"""
        with open(self.__file_name, encoding="utf-8") as f:
            original_json = json.load(f)
        new_json = []
        for item in original_json:
            if item["description"] is not None:
                if key_word in item["description"]:
                    new_json.append(item)
        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(new_json, f, ensure_ascii=False, indent=4)
        with open(self.__file_name, encoding="utf-8") as f:
            filtered_vacancies = json.load(f)
        return filtered_vacancies

    def delete_from_json(self, id_list: List) -> None:
        """Метод удалят ваканчию по заданному списку id"""
        with open(self.__file_name, encoding="utf-8") as f:
            original_json = json.load(f)
            new_json = []
            for item in original_json:
                if item["id"] not in id_list:
                    new_json.append(item)
        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(new_json, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    python1 = HH()
    python1.get_vacancies("python")
    #    id_list_1 = ['105372844', '105832342', '95074564', '102916032', '103114737']
    list_1 = python1.vacancies
    json_1 = WorkWithJson()
    json_1.save_to_json(list_1)
#   key_word_1 = "небольших"
#   json_1.get_data_from_json(key_word_1)
#   json_1.delete_from_json(id_list_1)"""
