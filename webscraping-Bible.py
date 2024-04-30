import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


x = random.randint(1,21)

if x >= 10:
    x=x
if x < 10:
    x=f'0{x}'

webpage = f'https://ebible.org/asv/JHN{x}.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

page = urlopen(req)

soup = BeautifulSoup(page, 'html.parser')

whole_chapter = soup.findAll('div', attrs={'class':'p'})

my_verses = []

for y in whole_chapter:
    verselist = y.text.split('.')
    
    for w in verselist:
        o = w.split('?')
        for n in o:
            l = n.split('!')
            for t in l:
                t.strip('[]').strip("''").strip('\xa0')
                my_verses.append(t)

my_verses = [i for i in my_verses if i != ' ']

randomverse = random.choice(my_verses)

print(f'Chapter: {x} Verse:{randomverse}')


