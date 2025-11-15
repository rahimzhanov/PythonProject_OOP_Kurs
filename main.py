from src.hh_api import HeadHunterApi
from src.json_saver import JsonSaver
from src.utils import sort_vacancies, get_top_vacancies, print_vacancies



def user_interaction():
    """
    Основная функция взаимодействия с пользователем.
    Собирает все компоненты программы в единый рабочий процесс.
    """
    print("🎯 Программа для поиска вакансий с HeadHunter")
    print("=" * 50)

    # 1. Получаем параметры поиска от пользователя
    search_query = input("Введите поисковый запрос: ").strip()
    if not search_query:
        print("❌ Поисковый запрос не может быть пустым")
        return

    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        if top_n <= 0:
            print("❌ Количество вакансий должно быть положительным числом")
            return
    except ValueError:
        print("❌ Пожалуйста, введите целое число")
        return

    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()
    min_salary_input = input("Введите минимальную зарплату (оставьте пустым если не важно): ").strip()

    # 2. Инициализируем компоненты
    hh_api = HeadHunterApi()
    json_saver = JsonSaver()

    print("\n🔍 Ищем вакансии...")

    # 3. Получаем вакансии с HH.ru
    try:
        raw_vacancies = hh_api.fetch_vacancies(search_query)
        vacancies_list = HeadHunterApi.format_vacancies(raw_vacancies)

        if not vacancies_list:
            print("❌ По вашему запросу вакансий не найдено")
            return

        print(f"✅ Найдено {len(vacancies_list)} вакансий с HeadHunter")

    except Exception as e:
        print(f"❌ Ошибка при получении вакансий: {e}")
        return

    # 4. Сохраняем вакансии в файл
    print("💾 Сохраняем вакансии в файл...")
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    # 5. Подготавливаем фильтры для поиска в сохраненных данных
    filters = {}

    if filter_words:
        filters['keywords'] = filter_words
        print(f"🔤 Фильтруем по ключевым словам: {', '.join(filter_words)}")

    if min_salary_input:
        try:
            filters['min_salary'] = int(min_salary_input)
            print(f"💰 Фильтруем по минимальной зарплате: {min_salary_input} руб.")
        except ValueError:
            print("⚠️  Минимальная зарплата не распознана, продолжаем без фильтрации по зарплате")

    # 6. Получаем отфильтрованные вакансии из файла
    filtered_vacancies = json_saver.get_vacancies(filters)

    if not filtered_vacancies:
        print("❌ После фильтрации вакансий не найдено")
        return

    print(f"✅ После фильтрации осталось {len(filtered_vacancies)} вакансий")

    # 7. Сортируем и выбираем топ N
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(top_n, sorted_vacancies)

    print(f"\n🏆 Топ-{len(top_vacancies)} вакансий по зарплате:")
    print("=" * 50)

    # 8. Выводим результат
    print_vacancies(top_vacancies)


def main():
    """
    Главная функция программы с обработкой исключений.
    """
    try:
        user_interaction()
    except KeyboardInterrupt:
        print("\n\n👋 Программа завершена пользователем")
    except Exception as e:
        print(f"\n💥 Произошла непредвиденная ошибка: {e}")
    finally:
        print("\n✨ Спасибо за использование программы!")


if __name__ == "__main__":
    main()