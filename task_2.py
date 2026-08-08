def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []
    cats = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            cat_id, name, age = line.split(",")
        except ValueError:
            continue
        cats.append({"id": cat_id, "name": name, "age": age})
    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
