import re
from functools import reduce
from google.colab import files


print("Загрузите файл Dostoevsky.txt")
uploaded = files.upload()
filename = list(uploaded.keys())[0]
text = uploaded[filename].decode("utf-8")


PATTERN = r'[А-ЯЁ]\.\s(?:[А-ЯЁ]\.\s)?[А-ЯЁ][а-яё]+'

find_matches   = lambda t: re.findall(PATTERN, t)
deduplicate    = lambda lst: list(reduce(
    lambda acc, x: acc if x in acc else acc + [x], lst, []
))
format_results = lambda matches: "\n".join(
    map(lambda item: f"{item[0]+1}. {item[1]}", enumerate(matches))
)

matches = find_matches(text)
unique  = deduplicate(matches)

print(f"\nНайдено вхождений: {len(matches)}")
print(f"Уникальных: {len(unique)}")
print("\n--- Все уникальные фамилии с инициалами ---")
print(format_results(unique))
