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
    if not vacancies:
        return []

    if len(vacancies) < n:
        n = len(vacancies)

    return vacancies[:n]


def print_vacancies(vacancies: List['Vacancy']) -> None:
    """
    Красиво выводит вакансии в консоль с нумерацией и разделителями

    Args:
        vacancies: Список вакансий для отображения
    """
    # Проверяем, есть ли вакансии для показа
    if not vacancies:
        print(" Вакансии не найдены")
        return

    # Проходим по всем вакансиям с нумерацией
    for index, vacancy in enumerate(vacancies, start=1):
        # Выводим номер вакансии
        print(f"🔹 Вакансия #{index}")
        print(f"   Название: {vacancy.name}")
        print(f"   Зарплата: от {vacancy.salary_from} до {vacancy.salary_to}")
        print(f"   Ссылка: {vacancy.url}")
        print(f"   Описание: {vacancy.description}")

        # Добавляем разделитель между вакансиями
        if index < len(vacancies):  # Не выводим после последней вакансии
            print("─" * 50)

    # Итоговая информация
    print(f"\n📊 Всего найдено вакансий: {len(vacancies)}")

