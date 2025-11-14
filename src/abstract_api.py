from abc import ABC, abstractmethod


class AbstractApi(ABC):

    @abstractmethod
    def _connect_to_api(self, keyword: str):
        pass

    @abstractmethod
    def fetch_vacancies(self, keyword: str):
        pass

    @staticmethod
    @abstractmethod
    def format_vacancies(self, raw_data: list[dict]) -> list[dict]:
        pass
