def get_cats_info(path):
  cats_info = []
  try:
    with open(path, "r", encoding="utf-8") as file:
      for line in file:
        line = line.strip()
        if not line:
          continue
        cat_id, name, age = line.split(",")
        cats_info.append({"id": cat_id, "name": name, "age": age})
    return cats_info
  except FileNotFoundError:
    print(f"Файл '{path}' не знайдено.")
    return []
  except ValueError:
    print("Помилка у форматі даних файлу.")
    return []

if __name__ == "__main__":
  cats_info = get_cats_info("cats_file.txt")
  print(cats_info)
