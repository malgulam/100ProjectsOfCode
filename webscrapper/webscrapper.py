#this is a simpler webscrapper that takes in input via terminal 
#and searches google for the results, parses it with bs4 
#and view results to users

from bs4 import BeautifulSoup as bs
import requests
import re
import time

search_choice = str(input(str('Would you like to use google as default?Y/N \n =>'))).lower()
if search_choice:
    if search_choice == 'y':
        pass
    else:
        #using yoda syntaxing here because can't come up with variable name
        print('Not using google as default.You will be prompted to type in the name\nof the website you want to scrape!')
        print('The website should follow this syntax: https://www.google.com/search?q=')
        print('protocol://www.domainname.domainnameExtension/getParameter?keywords')
        choice_search = input(str('what website are you looking to scrape?\n=>'))
        if choice_search:
            keyword_ = input(str('What keyword are you looking for in this website?\n=>').lower())
            print('Starting scrape')
            resp = requests.get(f'{choice_search}{keyword_}')
            soup  = bs(resp.content, 'html.parser')
            results = soup.body.find_all(string=re.compile(f'.*{keyword_}.*'), recursive=True)
            print(f'Found keyword: {keyword_} {len(results)} times')
            for i in range(len(results)):
                print(f'RESULT {i+1}: {results[i]}\n')
            print('end of results')
            exit(0)
        else:
            print('you need to choose a website to scrape!')
else:
    print('you need to answer the query!')
    exit(0)

#uses google.com as a default
print('using google as default!')
base_url = 'https://www.google.com/search?q='
keyword_  = input(str('What keyword are you scrapping\n=>'))
print('Starting scrape')
resp = requests.get(f'{base_url}{keyword_}')
soup = bs(resp.content, 'html.parser')
results = soup.body.find_all(string=re.compile(f'.*{keyword_}.*'), recursive=True)
if results:
    print(f'found keyword:{keyword_} {len(results)} times!')
    time.sleep(3)
    #for result in results:
    for i in range(len(results)):
        print(f'RESULT {i+1}: {results[i]}\n')
        #print(f'RESULT {results.index(result)}: {result}')
    print('end of results')
    exit(0)
else:
    print('no results found')
    exit(1)
