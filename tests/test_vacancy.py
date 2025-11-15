from src.vacancy import Vacancy


class TestVacancy:
    """Тесты для класса Vacancy"""

    def test_vacancy_creation(self):
        """Тест создания вакансии с указанной зарплатой"""
        vacancy = Vacancy(
            name="Python Developer",
            salary={"from": 100000, "to": 150000},
            url="https://hh.ru/vacancy/123",
            description="Разработка на Python"
        )

        assert vacancy.name == "Python Developer"
        assert vacancy.salary_from == 100000
        assert vacancy.salary_to == 150000
        assert vacancy.url == "https://hh.ru/vacancy/123"
        assert vacancy.description == "Разработка на Python"

    def test_vacancy_without_salary(self):
        """Тест создания вакансии без зарплаты"""
        vacancy = Vacancy(
            name="Python Developer",
            salary=None,
            url="https://hh.ru/vacancy/123",
            description="Разработка на Python"
        )

        assert vacancy.salary_from == 0
        assert vacancy.salary_to == 0

    def test_vacancy_comparison(self):
        """Тест сравнения вакансий по зарплате"""
        vacancy1 = Vacancy("Developer1", {"from": 100000, "to": 150000}, "url1", "desc1")
        vacancy2 = Vacancy("Developer2", {"from": 150000, "to": 200000}, "url2", "desc2")

        assert vacancy2 > vacancy1
        assert vacancy1 < vacancy2
