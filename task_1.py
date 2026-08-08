def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    continue

    except FileNotFoundError:
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count
    return total, int(average) if average.is_integer() else average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
