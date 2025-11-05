from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class AbstractSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        pass

    @abstractmethod
    def get_vacancies(self, filters: dict = None) -> list['Vacancy']:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: 'Vacancy') -> None:
        pass