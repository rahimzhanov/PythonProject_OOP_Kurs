from typing import Any, Dict

import requests
from src.abstract_api import AbstractApi

from src.vacancy import Vacancy


class HeadHunterApi(AbstractApi):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Инициализирует параметры для подключения к API HeadHunter."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"per_page": 5}

    def _connect_to_api(self, keyword: str) -> Dict[str, Any]:
        """
        Устанавливает соединение с API HeadHunter.

        Args:
            keyword: Ключевое слово для поиска вакансий

        Returns:
            Ответ API в формате JSON

        Raises:
            requests.HTTPError: При ошибке HTTP-запроса
        """
        self.__params['text'] = keyword
        response = requests.get(self.__url, params=self.__params)
        response.raise_for_status()
        return response.json()

    def fetch_vacancies(self, keyword: str) -> list[dict]:
        """
        Получает список вакансий по ключевому слову.

        Args:
            keyword: Ключевое слово для поиска

        Returns:
            Список словарей с данными вакансий
        """
        response = self._connect_to_api(keyword)
        return response['items']

    @staticmethod
    def format_vacancies(all_vacancies):
        """
        Преобразует сырые данные вакансий в список объектов Vacancy.

        Args:
            all_vacancies: Список сырых данных вакансий из API

        Returns:
            Список объектов Vacancy
        """
        vacancies = []
        for vacancy in all_vacancies:
            vac = Vacancy(
                name=vacancy['name'],
                salary=vacancy['salary'],
                description=vacancy['snippet'].get("responsibility"),
                url=vacancy["alternate_url"]
            )
            vacancies.append(vac)
        return vacancies


if __name__ == '__main__':

    hh = HeadHunterApi()
    vacs = hh.fetch_vacancies('python')
    formatted_vacs = HeadHunterApi.format_vacancies(vacs)
    for vac in formatted_vacs:
        print(vac)
