from abc import ABC, abstractmethod


class AbstractApi(ABC):

    def _connect_to_api(self, keyword):
        pass


    @abstractmethod
    def get_vacancies(self, keyword):
        pass


    @abstractmethod
    def format_vacancies(self):
        pass