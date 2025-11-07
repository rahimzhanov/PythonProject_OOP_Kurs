import json
from utils import sort_vacancies
from typing import List, Dict, Any

from abstract_saver import AbstractSaver
from src.vacancy import Vacancy


class JsonSaver(AbstractSaver):

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename


    @staticmethod
    def _apply_filters(vacancies: list[Vacancy], filters: dict) -> list[Vacancy]:
        """Применяет фильтры к списку вакансий (внутренний метод)"""
        filtered = []
        for vacancy in vacancies:
            # Фильтр по минимальной зарплате
            if 'min_salary' in filters and vacancy.salary_from < filters['min_salary']:
                continue

            # Фильтр по ключевым словам
            if 'keywords' in filters:
                keywords = [kw.lower() for kw in filters['keywords']]
                description = vacancy.description.lower()
                if not any(keyword in description for keyword in keywords):
                    continue

            filtered.append(vacancy)
        return filtered


    def get_vacancies(self, filters: dict = None) -> list[Vacancy]:
        """Получение данных из файла"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as files:
                data = json.load(files)

            vacancies = []
            for vacancy_data in data:
                vacancy = Vacancy(
                    name=vacancy_data['name'],
                    salary=vacancy_data.get('salary'),
                    url=vacancy_data.get('url'),
                    description=vacancy_data['description']
                )
                vacancies.append(vacancy)

            if filters:
                vacancies = self._apply_filters(vacancies, filters)
            return vacancies

        except FileNotFoundError:
                print(f"Файл {self.__filename} не найден")
                return []

        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.__filename}")
            return []

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из JSON файла по ссылке"""
        try:
            # 1. Читаем все вакансии из файла
            with open(self.__filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # 2. Оставляем только те вакансии, у которых ссылка НЕ совпадает
            new_data = [v for v in data if v['url'] != vacancy.url]

            # 3. Если ничего не удалили - выходим
            if len(new_data) == len(data):
                print(f"Вакансия с ссылкой {vacancy.url} не найдена")
                return

            # 4. Записываем обновленные данные обратно
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=2)

            print(f"Вакансия '{vacancy.name}' удалена")

        except FileNotFoundError:
            print(f"Файл {self.__filename} не найден")
        except Exception as e:
            print(f"Ошибка при удалении вакансии: {e}")



    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление списка"""
        try:
            try:
                with open(self.__filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Если файла нет - начинаем с пустого списка
                data = []

            vacancy_dict = {
                'name': vacancy.name,
                'salary': {'from': vacancy.salary_from, 'to': vacancy.salary_to},
                'url': vacancy.url,
                'description': vacancy.description
            }

            # Ищем дубликат по ссылке
            for existing_vacancy in data:
                if existing_vacancy['url'] == vacancy.url:
                    print(f"Вакансия '{vacancy.name}' уже существует")
                    return

            # 3. Добавляем новую вакансию
            data.append(vacancy_dict)

            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"Вакансия '{vacancy.name}' добавлена")

        except Exception as e:
            print(f"Ошибка при добавлении вакансии: {e}")

if __name__ == '__main__':
    # Сначала ПИШЕМ данные в файл, потом читаем
    saver = JsonSaver()

    # 1. Тест на пустой файл
    print("Тест 1 - Пустой файл:")
    result = saver.get_vacancies()
    print(f"Результат: {result}")  # Должен быть [] с сообщением "Файл не найден"

    # 2. Создадим тестовую вакансию и сохраним
    print("\nТест 2 - Добавление вакансии:")
    test_vacancy = Vacancy(
        name="Python Developer",
        salary={"from": 100000, "to": 150000},
        url="https://hh.ru/vacancy/123",
        description="Разработка на Python и Django"
    )
    saver.add_vacancy(test_vacancy)  # 👈 Это создаст файл
    test_vacancy2 = Vacancy(
        name="Dev",
        salary={"from": 200000, "to": 250000},
        url="https://hh.ru/vacancy/133",
        description="Разработка на Python "
    )
    saver.add_vacancy(test_vacancy2)
    # 3. Теперь читаем
    print("\nТест 3 - Чтение после добавления:")
    result = saver.get_vacancies()
    print(f"Найдено вакансий: {len(result)}")
    for vac in result:
        print(vac)

    print(sort_vacancies(result))
    # 4. Тест фильтров
    print("\nТест 4 - Фильтры:")
    filtered = saver.get_vacancies({"min_salary": 50000})
    print(f"После фильтра: {len(filtered)} вакансий")