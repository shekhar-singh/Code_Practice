from bs4 import BeautifulSoup, SoupStrainer
 
with open('page.txt','r') as f:
    for link in BeautifulSoup(f.read(), parse_only=SoupStrainer('a')): 
        if link.has_attr('href'): 
            print(link['href'])





#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)