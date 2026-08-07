def total_salary(path):
  try:
    with open(path, "r", encoding="utf-8") as file:
      salaries = []
      for line in file:
        line = line.strip()
        if not line:
          continue
        name, salary = line.split(",")
        salaries.append(int(salary))
    if not salaries:
      return (0, 0)
    total = sum(salaries)
    average = total / len(salaries)
    return (total, average)
  except FileNotFoundError:
    print(f"Файл '{path}' не знайдено.")
    return (0, 0)
  except ValueError:
    print("Помилка у форматі даних файлу.")
    return (0, 0)

if __name__ == "__main__":
  total, average = total_salary("salary_file.txt")
  print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
