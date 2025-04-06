import requests
import bs4

r = requests.get('https://www.canada.ca/en/department-finance/news/2025/03/list-of-products-from-the-united-states-subject-to-25-per-cent-tariffs-effective-march-13-2025.html')

soup = bs4.BeautifulSoup(r.text, 'html.parser')

# Find the table with tariffs
table = soup.find('table')

with open('tariffs.html', 'w') as f:
    f.write(table)