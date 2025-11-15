class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ['name', 'salary_from', 'salary_to', 'url', 'description']

    def __init__(self, name: str, salary, url: str, description: str):
        """
        Инициализирует объект вакансии.

        Args:
            name: Название вакансии
            salary: Данные о зарплате из API
            url: Ссылка на вакансию
            description: Описание вакансии
        """
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __validate_salary(self, salary: dict):
        """
        Валидирует и устанавливает значения зарплаты.

        Args:
            salary: Словарь с данными о зарплате из API
        """
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_to = 0
            self.salary_from = 0

    def __lt__(self, other):
        """
        Сравнивает вакансии по минимальной зарплате (меньше).

        Args:
            other: Другая вакансия для сравнения

        Returns:
            bool: True если текущая вакансия имеет меньшую минимальную зарплату
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        Сравнивает вакансии по минимальной зарплате (больше).

        Args:
            other: Другая вакансия для сравнения

        Returns:
            bool: True если текущая вакансия имеет большую минимальную зарплату
        """
        return self.salary_from > other.salary_from

    def __str__(self):
        """
        Возвращает строковое представление вакансии.

        Returns:
            Строка с основной информацией о вакансии
        """
        return (f'Название вакансии: {self.name}, зарплата от {self.salary_from} до '
                f'{self.salary_to}, ссылка: {self.url}, описание:{self.description}')

    def __repr__(self):
        """
        Возвращает формальное строковое представление вакансии.

        Returns:
            Строка для отладки и представления объекта
        """
        return (f'Название вакансии: {self.name}, зарплата от {self.salary_from} до '
                f'{self.salary_to}, ссылка: {self.url}, описание:{self.description}')


if __name__ == '__main__':
    salary_data = {'from': 50000, 'to': 80000}
    vac = Vacancy("Python Developer", salary_data, "http://example.com", "Описание вакансии")
    print(vac)
