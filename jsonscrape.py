from bs4 import BeautifulSoup
import requests
import csv
import json

with open('shufflelabssitemap.json') as f:
  sitemap = json.load(f)
  
print(sitemap)
source = requests.get(sitemap['startUrl'][0]).text
#print(source)

soup = BeautifulSoup(source, 'lxml')

num_selectors = len(sitemap['selectors'])

i = num_selectors

with open('sitemap_data.csv', 'w') as f:
    for selector in sitemap['selectors']:
        #print(selector['id'])
        i = i-1
        if(i != 0):
            f.write(selector['id'] + ',')
        else:
            f.write(selector['id'])

for selector in sitemap['selectors']:
    if(selector['type'] == 'SelectorText'):
        selector_arr = [selector['selector']]
        selector_arr = [char for element in selector_arr for char in element.split(', ')]
        #print(selector_arr)
        for element in selector_arr:
            element_arr = [element]
            element_arr = [x for y in element_arr for x in y.split(' ')]
            element_arr = [x for y in element_arr for x in y.split('.')]
            for string in element_arr:
                if(string == ''):
                    element_arr.pop(element_arr.index(string))
            #print(element_arr)
            element_arr2 = element_arr
            if(element_arr[0] != 'p' and element_arr[0] != 'h1' and element_arr[0] != 'h2' and element_arr[0] != 'a' and element_arr[0] != 'li' and element_arr[0] != 'ul' and element_arr[0] != 'ol' and element_arr[0] != 'span'):
                firstel = element_arr[0]
                string_arr = ['item.']
                if(len(element_arr) > 0):
                    element_arr.pop(0)
                while(len(element_arr) > 0):
                    if(len(element_arr) == 1):
                        string_arr.append(element_arr[0])
                    else:
                        string_arr.append(element_arr[0])
                        string_arr.append('.')
                    element_arr.pop(0)
                #string_arr.append(element_arr[0])
                string_arr.append('.text')
                #print(string_arr)
                string = ''.join(string_arr)
                #print(string)
                #print(firstel)
                for item in soup.find_all(class_ = firstel):
                    headline = eval(string)
                    print(headline)
            else:
                print(1)
    elif(selector['type'] == 'SelectorLink'):
        selector_arr = [selector['selector']]
        selector_arr = [char for element in selector_arr for char in element.split(', ')]
        #print(selector_arr)
        for element in selector_arr:
            element_arr = [element]
            element_arr = [x for y in element_arr for x in y.split(' ')]
            element_arr = [x for y in element_arr for x in y.split('.')]
            for string in element_arr:
                if(string == ''):
                    element_arr.pop(element_arr.index(string))
            #print(element_arr)
            element_arr2 = element_arr
            if(element_arr[0] != 'p' and element_arr[0] != 'h1' and element_arr[0] != 'h2' and element_arr[0] != 'a' and element_arr[0] != 'li' and element_arr[0] != 'ul' and element_arr[0] != 'ol' and element_arr[0] != 'span'):
                firstel = element_arr[0]
                string_arr = ['item.']
                if(len(element_arr) > 0):
                    element_arr.pop(0)
                while(len(element_arr) > 0):
                    if(len(element_arr) == 1):
                        string_arr.append(element_arr[0])
                    else:
                        string_arr.append(element_arr[0])
                        string_arr.append('.')
                    element_arr.pop(0)
                #string_arr.append(element_arr[0])
                string_arr.append('[\'href\']')
                #print(string_arr)
                string = ''.join(string_arr)
                #print(string)
                #print(firstel)
                for item in soup.find_all(class_ = firstel):
                    headline = eval(string)
                    print(headline)