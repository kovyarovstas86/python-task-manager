"""Простой консольный менеджер задач."""

tasks = []


def add_task(title):
    """Добавляет задачу в список."""
    if not title.strip():
        return False
    tasks.append(title.strip())
    return True


def show_tasks():
    """Возвращает список задач с номерами."""
    if not tasks:
        return "Список задач пуст."
    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks, start=1))


def remove_task(number):
    """Удаляет задачу по номеру. Нумерация начинается с 1."""
    if not isinstance(number, int) or number < 1 or number > len(tasks):
        return False
    tasks.pop(number - 1)
    return True


def main():
    while True:
        print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите задачу: ")
            print("Задача добавлена." if add_task(title) else "Пустую задачу добавить нельзя.")
        elif choice == "2":
            print(show_tasks())
        elif choice == "3":
            print(show_tasks())
            try:
                number = int(input("Номер задачи для удаления: "))
                print("Задача удалена." if remove_task(number) else "Неверный номер.")
            except ValueError:
                print("Нужно ввести целое число.")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
