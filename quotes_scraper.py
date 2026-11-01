import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
header= {"User-Agent": "Rozie practice cot. contact: rozie@gmail.com"}
response= requests.get(URL, headers=header, timeout=10)
soup= BeautifulSoup(response.content, "html.parser")
cards= soup.select(".quote")
all_quotes=[]
for quote in cards:
    text= quote.select_one(".text").text
    author= quote.select_one(".author").text
    tags=[]
    for tag in quote.select(".tag"):
        tags.append(tag.text)
    quote_item={"Quote": text, "person": author, "tags":tags}
    all_quotes.append(quote_item)
print(all_quotes)
'''
#print(cards)
first= cards[0]
#print(first.select_one(".text").text)
#print(first.select_one(".author").text)
#tags=first.select(".tag")
#print(tags[0].text)
tags=[]
for tag in first.select(".tag"):
    tags.append(tag.text)
print(tags)
'''
