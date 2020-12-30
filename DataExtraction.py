from bs4 import BeautifulSoup
import requests
import json
import config

class DataExtraction:
    def html_tags(self, element_arr):   # bool function checks if first element of data is html tag
        if(element_arr[0] == 'p' or element_arr[0] == 'h1' or element_arr[0] == 'h2' or element_arr[0] == 'a' or element_arr[0] == 'li' or element_arr[0] == 'ul' or element_arr[0] == 'ol' or element_arr[0] == 'span'):
            return True
        else:
            return  False
        
    def get_start_URL(self,file):
        with open(file) as f:
            config.sitemap = json.load(f) # loads sitemap variable with json
        config.startUrl = config.sitemap['startUrl'][0]
        
    def get_soup(self, file): # open file and get soup
        DataExtraction.get_start_URL(DataExtraction, file)
        config.source = requests.get(config.startUrl).text
        config.soup = BeautifulSoup(config.source, 'lxml')
        
    # def write_csv_headers(self):    # writes csv headers
    #     num_selectors = len(config.sitemap['selectors'])
    #     i = num_selectors
    #     with open('sitemap_data.csv', 'w') as f:
    #         # for selector in config.sitemap['selectors']:
    #         #     i = i-1
    #         #     if(i != 0):
    #         #         f.write(selector['id'] + ',')
    #         #     else:
    #         #         f.write(selector['id'])
    #         for selector in config.sitemap['selectors']:
    #                 f.write(selector['id'] + ',')
                    
    def create_extraction_elements(self, file):   # algorithm to use given selectors to convert into string which is used in  each Selectortype class
        DataExtraction.get_soup(DataExtraction, file)
        #DataExtraction.write_csv_headers(DataExtraction)
        for selector in config.sitemap['selectors']:
            if(selector['parentSelectors'][0] != '_root'):
                for selector2 in config.sitemap['selectors']:
                    if(selector['parentSelectors'][0] == selector2['id']):
                        if(selector2['type'] == 'SelectorLink'):
                            print(1)
            selector_arr = [selector['selector']]
            selector_arr = [char for element in selector_arr for char in element.split(', ')]
            for element in selector_arr:
                element_arr = [element]
                element_arr = [x for y in element_arr for x in y.split(' ')]
                element_arr = [x for y in element_arr for x in y.split('.')]
                for string in element_arr:
                    if(string == ''):
                        element_arr.pop(element_arr.index(string))
                #print(element_arr)
                if(len(element_arr) == 1):
                    config.firstels[selector['type']].append(element_arr[0])
                    element_arr.pop(0)
                else:
                    if(DataExtraction.html_tags(DataExtraction, element_arr)):
                        element_arr.pop(0)
                    #print(element_arr)
                    config.firstels[selector['type']].append(element_arr[0])
                    element_arr.pop(0)
                string_arr = ['item']
                while(len(element_arr) > 0):
                    string_arr.append('.')
                    string_arr.append(element_arr[0])
                    element_arr.pop(0)
                string = ''.join(string_arr)
                config.output_dict[selector['type']][selector['id']].append(string)
        #print(config.output_dict)
