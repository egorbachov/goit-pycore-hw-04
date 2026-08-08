def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return 0, 0
    total = 0
    count = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            name, salary = line.split(",")
            total += int(salary)
            count += 1
        except ValueError:
            continue
    if count == 0:
        return 0, 0
    average = total / count
    return total, int(average) if average.is_integer() else average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
