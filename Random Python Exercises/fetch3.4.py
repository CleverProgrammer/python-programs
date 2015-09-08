import requests
import BeautifulSoup

session = requests.session()

req = session.get('http://stackoverflow.com/questions/10807081/script-to-extract-data-from-wbpage')

doc = BeautifulSoup.BeautifulSoup(req.content)

print (doc.findAll('a', { "class" : "gp-share" }))
