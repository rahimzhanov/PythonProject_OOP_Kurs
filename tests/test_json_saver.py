import pytest
import os
import json
from src.vacancy import Vacancy
from src.json_saver import JsonSaver


class TestJsonSaver:
    """Тесты для класса JsonSaver"""

    def test_add_and_get_vacancy(self, tmp_path):
        """Тест добавления и получения вакансии"""
        test_file = tmp_path / "test_vacancies.json"
        saver = JsonSaver(str(test_file))

        vacancy = Vacancy(
            name="Python Developer",
            salary={"from": 100000, "to": 150000},
            url="https://hh.ru/vacancy/123",
            description="Python development"
        )

        # Добавляем вакансию
        saver.add_vacancy(vacancy)

        # Получаем вакансии
        vacancies = saver.get_vacancies()

        assert len(vacancies) == 1
        assert vacancies[0].name == "Python Developer"
        assert vacancies[0].salary_from == 100000

    def test_filter_by_salary(self, tmp_path):
        """Тест фильтрации по зарплате"""
        test_file = tmp_path / "test_vacancies.json"
        saver = JsonSaver(str(test_file))

        vacancy1 = Vacancy("Low", {"from": 50000}, "url1", "desc1")
        vacancy2 = Vacancy("High", {"from": 150000}, "url2", "desc2")

        saver.add_vacancy(vacancy1)
        saver.add_vacancy(vacancy2)

        # Фильтруем по минимальной зарплате
        filtered = saver.get_vacancies({"min_salary": 100000})

        assert len(filtered) == 1
        assert filtered[0].name == "High"

    def test_delete_vacancy(self, tmp_path):
        """Тест удаления вакансии"""
        test_file = tmp_path / "test_vacancies.json"
        saver = JsonSaver(str(test_file))

        vacancy = Vacancy("Python Dev", {"from": 100000}, "https://test.com", "desc")
        saver.add_vacancy(vacancy)

        # Удаляем вакансию
        saver.delete_vacancy(vacancy)

        # Проверяем что вакансий нет
        vacancies = saver.get_vacancies()
        assert len(vacancies) == 0