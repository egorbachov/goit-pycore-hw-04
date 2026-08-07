def total_salary(path):
  try:
    with open(path, "r", encoding="utf-8") as file:
      lines = file.readlines()
  except FileNotFoundError:
    return 0, 0
  total = 0
  for line in lines:
    name, salary = line.split(",")
    total += int(salary)
  average = total / len(lines)
  return total, average

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
