# Подключаем библиотеку requests для работы с интернет-запросами
import requests

# Подключаем BeautifulSoup для анализа HTML-кода
from bs4 import BeautifulSoup

# Отправляем запрос на сайт VK Ads, получаем содержимое страницы
page = requests.get("https://ads.vk.com/cases")

# Создаем версию HTML для поиска элементов
soup = BeautifulSoup(page.content, 'html.parser')

# Создаем список для хранения информации о кейсах
cases = [
    # Для каждой найденной карточки создаем словарь с 3 полями
    {
        # Находим внутри карточки изображение и берем его описание (alt)
        'title': card.find('img')['alt'],
        
        # Берем ссылку из карточки и делаем ее полной (добавляем https://ads.vk.com)
        'link': f"https://ads.vk.com{card['href']}",
        
        # Ищем тег <time>, берем дату, если нет - пишем "Дата не указана"
        'date': card.find('time').get('datetime', 'Дата не указана')
    }
    # Находим ВСЕ элементы <a> с классом case-card_wrapper__F9fy_ на странице
    for card in soup.find_all('a', class_='case-card_wrapper__F9fy_')
]

# Показываем заголовок перед выводом данных
print("Список словарей с кейсами:")

# Перебираем все собранные кейсы по одному
for case in cases:
    # Выводим информацию о каждом кейсе
    print(case)

# Показываем итоговое количество найденных кейсов
print(f"\nВсего собрано: {len(cases)} кейсов")
