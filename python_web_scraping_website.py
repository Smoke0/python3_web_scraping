import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)


soup = BeautifulSoup(response.text,'html.parser')
one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']
download_url = 'http://web.mta.info/developers/' + link
some = urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
print(some)
time.sleep(1)