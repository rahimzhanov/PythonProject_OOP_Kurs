class Vacancy:
    __slots__ = ['name', 'salary_from', 'salary_to', 'url', 'description']

    def __init__(self, name: str, salary, url: str, description: str):
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def  __validate_salary(self, salary: dict):
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to']
        else:
            self.salary_to = 0
            self.salary_from = 0


    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __str__(self):
        return f'Название вакансии: {self.name}, зарплата от {self.salary_from} до {self.salary_to}, ссылка: {self.url}, описание:{self.description}'


if __name__ == '__main__':
    salary_data = {'from': 50000, 'to': 80000}
    vac = Vacancy("Python Developer", salary_data, "http://example.com", "Описание вакансии")
    print(vac)