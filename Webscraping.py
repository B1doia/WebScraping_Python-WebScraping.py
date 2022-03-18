import urllib.request
#biblioteca para consultar URL
from bs4 import BeautifulSoup
#funções BeautifulSoup para analizar dados retornados do site

wiki = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'
# local dos dados
page = urllib.request.urlopen(wiki)
#consultando site
soup = BeautifulSoup(page, 'html5lib')

list_item = soup.find('li', attrs={'class': 'toclevel-2 tocsection-26'})
name = list_item.text.strip()

print(name)
