import requests
url = 'https://dog.ceo/api/breed/random/image'
file_name = 'random_dogs.txt'
dog_links = []
for i in range(5):
    r = requests.get(url)
    data = r.json()
    dog_links = data['message']
    if data ['status'] == 'success':
        dog_links.append(data['message'])
        print(f'{i+1}. {data['message']}')
with open('random_dogs.txt', 'w') as f:
    for link in dog_links:
        f.write(link + '\n')

import requests
url = 'https://dog.ceo/api/breeds/list/all'
file_name = 'all_breeds.txt'
r = requests.get(url)
data = r.json()
breeds_dict = data['message']
breeds = list(breeds_dict.keys())
print('10пород')
for i, breed in enumerate(breeds[:10], 1):
    print(f"{i}. {breed}")
total = len(breeds)
print(f"\nВсего пород: {total}")
with open(file_name, "w") as file:
    for i, breed in enumerate(breeds, 1):
        file.write(f"{i}. {breed}\n")
print(f"\n✓ Все породы сохранены в {file_name}")

import requests
breed = input("Введите породу собаки: ").lower
url = f"https://dog.ceo/api/breed/{breed}/images"
r = requests.get(url)
data = r.json()
if data["status"] != "success":
    print(f"Порода '{breed}' не найдена.")
    exit()
images = data["message"]
total = len(images) 
print(f"Найдено {total} фотографий")
print("Первые 5:")
for i, link in enumerate(images[:5], 1):
    print(f"{i}. {link}")
file_name = "breed_photos.txt"
with open(file_name, "w") as file:
    for i, link in enumerate(images, 1):
        file.write(f"{i}. {link}\n")
print(f"\n✓ {total} фотографий сохранено в {file_name}")

import requests
breeds = ['labrador', 'golden', 'husky', 'bulldog', 'poodle']
results = {}
for breed in breeds:
    api_url = f"https://dog.ceo/api/breed/{breed}/images"
    response = requests.get(api_url)
    data = response.json()
    if data["status"] != "success":
        print(f"Порода '{breed}' не найдена.")
        results[breed] = 0
    else:
        results[breed] = len(data["message"])
header = "Порода          | Кол-во фотографий"
line = "─────────────────────────────────"
table_lines = [header, line]
for breed, count in results.items():
    table_lines.append(f"{breed:<15} | {count}")
max_breed = max(results, key=results.get)
min_breed = min(results, key=results.get)
table_lines.append("")
table_lines.append(f"Максимум: {max_breed} ({results[max_breed]} фотографий)")
table_lines.append(f"Минимум: {min_breed} ({results[min_breed]} фотографий)")
print("\n".join(table_lines))
file_name = "breeds_comparison.txt"
with open(file_name, "w") as file:
    file.write("\n".join(table_lines))
print(f"\n✓ Результаты сохранены в {file_name}")

import requests
url = "https://dog.ceo/api/breeds/list/all"
file_name = "breeds_report.txt"
r = requests.get(url)
data = r.json()
breeds = data["message"]
breeds_with_sub = {}
for breed, subbreeds in breeds.items():
    if len(subbreeds) > 0:
        breeds_with_sub[breed] = subbreeds
print("Породы с подпородами:\n")
for breed, subs in breeds_with_sub.items():
    print(f"{breed} — {', '.join(subs)}")