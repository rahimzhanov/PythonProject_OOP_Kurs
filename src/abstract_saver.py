from abc import ABC, abstractmethod


class AbstractSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict = None) -> list['Vacancy']:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: 'Vacancy') -> None:
        pass

    @abstractmethod
    def add_vacancies(self, vacancies: list["Vacancy"]) -> None:
        pass