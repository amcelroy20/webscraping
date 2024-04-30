from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

authordict = {}
lengthdict = {}
lengthlist = []
tagslist = []
tagsdict = {}

for x in range(1,11):
    url = f'https://quotes.toscrape.com/page/{x}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(url, headers=headers)

    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')

    all_data = soup.findAll('div', attrs={'class':'quote'})


    for y in all_data:
        quote_text = y.find(attrs={'class':'text'}).text.strip('“').strip('”')
        lengthdict[quote_text]=(len(quote_text))
        lengthlist.append(len(quote_text))

        author = y.find(attrs={'class':'author'}).text
        if author not in authordict:
            authordict[author] = 0
        authordict[author]+=1

        tags = y.find(attrs={'class':'tags'}).text.strip('\n').strip(' ').strip('Tags:').strip('\n').strip(' ').strip('\n')
        taglist = tags.split('\n')
        for l in taglist:
            tagslist.append(l)

for key in authordict:
    print(f'Author: {key}')
    print(f'Number of Times Quoted: {authordict[key]}')
    print()

mostquoted = max(authordict, key=authordict.get)
leastquoted = min(authordict, key=authordict.get)
print(f'Most Quoted Author is: {mostquoted}')
print()
print(f'Least Quoted Author is: {leastquoted}')
print()
print()

avglength = sum(lengthlist)/len(lengthlist)
longestquote = max(lengthdict, key=lengthdict.get)
shortestquote = min(lengthdict, key=lengthdict.get)
print(f'Average length of quote is: {avglength:.2f} characters')
print()
print(f'Longest Quote is: {longestquote} at {lengthdict[longestquote]} characters')
print()
print(f'Shortest Quote is: {shortestquote} at {lengthdict[shortestquote]} characters')
print()
print()

repeatcount = 0
mostcommontag = ''
for tag in tagslist:
    if tag !='' and tag != 'attributed-no-source':
        k = [t for t in tagslist if t == tag]
        if len(k)>repeatcount:
            mostcommontag = tag
            repeatcount = len(k)
        tagsdict[tag] = len(k)

tagcount = len(tagslist)
print(f'The number of tags used was: {tagcount}')
print()
print(f'The most common tag was {mostcommontag}, appearing {repeatcount} times.')


from plotly.graph_objs import Bar
from plotly import offline

sorted_authors = sorted(authordict.items(), key=lambda x: x[1], reverse=True)

authors, quotes = [], []

for name, quotecount in sorted_authors[:10]:
    authors.append(name)
    quotes.append(quotecount)

data = [
    {
        'type':'bar',
        'x': authors,
        'y': quotes,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width':1.5, 'color':'rgb(25,25,25)'}
        },
        'opacity':0.6,
    }
]

my_layout = {
    'title': 'Most Quoted Authors on Website',
    'xaxis': {'title':'Authors'},
    'yaxis':{'title':'Times Quoted'}
}

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='author_graph.html')



sorted_tags = sorted(tagsdict.items(), key=lambda x: x[1], reverse=True)

tagname, tagnumber = [], []

for ta, gcount in sorted_tags[:10]:
    tagname.append(ta)
    tagnumber.append(gcount)

data2 = [
    {
        'type':'bar',
        'x': tagname,
        'y': tagnumber,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width':1.5, 'color':'rgb(25,25,25)'}
        },
        'opacity':0.6,
    }
]

my_layout2 = {
    'title': 'Most Used Tags on Website',
    'xaxis': {'title':'Tags'},
    'yaxis':{'title':'Times Used'}
}

fig2 = {'data':data2, 'layout':my_layout2}

offline.plot(fig2, filename='tag_graph.html')