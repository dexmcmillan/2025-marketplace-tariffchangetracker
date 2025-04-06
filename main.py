import requests

r = requests.get('https://www.canada.ca/en/department-finance/news/2025/03/list-of-products-from-the-united-states-subject-to-25-per-cent-tariffs-effective-march-13-2025.html')

with open('tariffs.html', 'w') as f:
    f.write(r.text)