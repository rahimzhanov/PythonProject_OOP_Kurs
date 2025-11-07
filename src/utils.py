from typing import List


def sort_vacancies(vacancies: List['Vacancy']) -> List['Vacancy']:
    """
    Сортирует список вакансий по убыванию зарплаты.

    Вакансии сортируются от самой высокой к самой низкой зарплате
    на основе поля salary_from класса Vacancy.
    """
    return sorted(vacancies, reverse=True)

def get_top_vacancies(n: int, vacancies: List['Vacancy']) -> List['Vacancy']:
    """
    Возвращает список топ N вакансий
    :param n:
    :param vacancies:
    :return: list
    """
    sorted_list = sort_vacancies(vacancies)
    return sorted_list[:n]
