from src.hh_api import HeadHunterApi


class TestHeadHunterApi:
    """Тесты для класса HeadHunterApi"""

    def test_api_initialization(self):
        """Тест инициализации API"""
        api = HeadHunterApi()

        # Проверяем что объект создан и имеет нужные атрибуты
        assert hasattr(api, '_HeadHunterApi__url')
        assert hasattr(api, '_HeadHunterApi__params')
        assert api._HeadHunterApi__params["per_page"] == 5

    def test_format_vacancies(self):
        """Тест форматирования вакансий"""
        api = HeadHunterApi()

        # Тестовые данные от HH API
        test_data = [
            {
                'name': 'Python Developer',
                'salary': {'from': 100000, 'to': 150000},
                'alternate_url': 'https://hh.ru/vacancy/123',
                'snippet': {'responsibility': 'Разработка на Python'}
            }
        ]

        formatted = api.format_vacancies(test_data)

        assert len(formatted) == 1
        vacancy = formatted[0]
        assert vacancy.name == 'Python Developer'
        assert vacancy.salary_from == 100000
        assert vacancy.url == 'https://hh.ru/vacancy/123'
