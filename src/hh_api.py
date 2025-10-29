import requests
from requests import Response
from src.abstract_api import AbstractApi


class HeadHunterApi(AbstractApi):
    def __init__(self) -> Response:
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"per_page": 20}


    def _connect_to_api(self, keyword):
        self.__params['text'] = keyword
        response = requests.get(self.__url, params=self.__params)
        response.raise_for_status()
        return response.json()


    def get_vacancies(self, keyword) -> list[dict]:
        pass


    def format_vacancies(self, raw_data: list[dict]) -> list[dict]:
        pass