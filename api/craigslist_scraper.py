from bs4 import BeautifulSoup
import requests


BASE_URL = 'http://chicago.craigslist.org/search/sss?query={0}'
def parse_results(search_term):
    results = []
    search_term = search_term.strip().replace(' ', '+')
    search_url = BASE_URL.format(search_term)
    r = requests.get(search_url)
    soup = BeautifulSoup(r.text)
    rows = soup.find('div', 'content').find_all('p', 'row')
    for row in rows:
        price = rows[0].find_all('span')[0].get_text()[1:]
        url = 'http://chicago.craigslist.org' + row.a['href']
        date = row.find_all('span')[3].get_text()[0:7]
        title = row.find_all('a')[1].get_text()
        results.append({'price': int(price), 'url': url, 'date': date, 'title': title})
    return results

