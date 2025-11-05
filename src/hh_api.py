from typing import Any, Dict

import requests
from src.abstract_api import AbstractApi
from  vacancy import Vacancy


class HeadHunterApi(AbstractApi):
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"per_page": 5}


    def _connect_to_api(self, keyword: str) -> Dict[str, Any]:
        self.__params['text'] = keyword
        response = requests.get(self.__url, params=self.__params)
        response.raise_for_status()
        return response.json()


    def fetch_vacancies(self, keyword: str) -> list[dict]:
        response = self._connect_to_api(keyword)
        return response['items']



    def format_vacancies(self, all_vacancies):
        vacancies = []
        for vacancy in all_vacancies:
            vac = Vacancy(
                name = vacancy['name'],
                salary = vacancy['salary'],
                description = vacancy['snippet'].get("responsibility"),
                url = vacancy["alternate_url"
                ])
            vacancies.append(vac)
        return vacancies


if __name__ == '__main__':

    hh = HeadHunterApi()
    vacs = hh.fetch_vacancies('python')
    formatted_vacs = hh.format_vacancies(vacs)
    for vac in formatted_vacs:
        print(vac)