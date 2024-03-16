def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1

        return total_salary, total_salary / num_developers if num_developers else 0

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except ValueError:
        print("Некоректний формат даних у файлі.")
        return None

# Приклад використання:
total, average = total_salary(r"D:\Projects\My_repo\H_Work_4\text1.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
