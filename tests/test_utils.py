import pytest
from src.vacancy import Vacancy
from src.utils import sort_vacancies, get_top_vacancies, print_vacancies


class TestUtils:
    """Тесты для утилитных функций"""

    def test_sort_vacancies(self):
        """Тест сортировки вакансий по зарплате"""
        vacancy1 = Vacancy("Low", {"from": 50000}, "url1", "desc1")
        vacancy2 = Vacancy("High", {"from": 150000}, "url2", "desc2")
        vacancy3 = Vacancy("Medium", {"from": 100000}, "url3", "desc3")

        vacancies = [vacancy1, vacancy2, vacancy3]
        sorted_list = sort_vacancies(vacancies)

        assert sorted_list[0] == vacancy2  # Самая высокая зарплата
        assert sorted_list[1] == vacancy3
        assert sorted_list[2] == vacancy1  # Самая низкая зарплата

    def test_get_top_vacancies(self):
        """Тест получения топ N вакансий"""
        vacancies = [
            Vacancy("V1", {"from": 100000}, "url1", "desc1"),
            Vacancy("V2", {"from": 200000}, "url2", "desc2"),
            Vacancy("V3", {"from": 300000}, "url3", "desc3")
        ]

        top_2 = get_top_vacancies(2, vacancies)
        assert len(top_2) == 2
        assert top_2[0] == vacancies[0]
        assert top_2[1] == vacancies[1]

    def test_get_top_more_than_exists(self):
        """Тест получения топа когда N больше количества вакансий"""
        vacancies = [
            Vacancy("V1", {"from": 100000}, "url1", "desc1"),
            Vacancy("V2", {"from": 200000}, "url2", "desc2")
        ]

        top_5 = get_top_vacancies(5, vacancies)
        assert len(top_5) == 2  # Должен вернуть все имеющиеся

    def test_get_top_empty_list(self):
        """Тест получения топа из пустого списка"""
        top_vacancies = get_top_vacancies(5, [])
        assert top_vacancies == []