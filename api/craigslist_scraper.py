from bs4 import BeautifulSoup
import requests


BASE_URL = 'http://chicago.craigslist.org/search/sss?query={0}'

def parse_results(search_term, max_price=0):
    results = []
    query = search_term.strip().replace(' ', '%20')
    search_url = BASE_URL.format(query)
    r = requests.get(search_url)
    soup = BeautifulSoup(r.text)
    rows = soup.find('div', 'content').find_all('p', 'row') 
    for row in rows:
     try:
      if int(row.span.string[1:]) < max_price or max_price == 0:
       url = 'http://chicago.craigslist.org' + row.a['href']
       price = row.span.string[1:]
       date = row.time.string
       title = row.find_all('a')[1].get_text()
       results.append({'price': int(price), 'url': url, 'date': date, 'title': title})
     except TypeError:
      continue
    cheapest = 0 
    for i, item in enumerate(results):
     if i == 0:
      cheapest = item['price']
     elif item['price'] < cheapest:
      item['price'] = cheapest
    print( "******************************************************")
    print( "***************** I found: %s results ****************" %len(results) )
    print( "***************** Cheapest %s: $%s ****************" %(search_term,cheapest))
    return results

def write_results(results):
    """Writes list of dictionaries to file."""
    fields = results[0].keys()
    with open('results.csv', 'w') as f:
        dw = csv.DictWriter(f, fieldnames=fields, delimiter='|')
        dw.writer.writerow(dw.fieldnames)
        dw.writerows(results)

def has_new_records(results):
    current_posts = [x['url'] for x in results]
    fields = results[0].keys()
    if not os.path.exists('results.csv'):
        return True

    with open('results.csv', 'r') as f:
        reader = csv.DictReader(f, fieldnames=fields, delimiter='|')
        seen_posts = [row['url'] for row in reader]

    is_new = False
    for post in current_posts:
        if post in seen_posts:
            pass
        else:
            is_new = True
    return is_new

def send_text(phone_number, msg):
    fromaddr = "Craigslist Checker"
    toaddrs = phone_number + "@txt.att.net"
    msg = ("From: {0}\r\nTo: {1}\r\n\r\n{2}").format(fromaddr, toaddrs, msg)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(config.email['username'], config.email['password'])
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
