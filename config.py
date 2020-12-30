#this file is basically global variables used/edited in all files

from collections import defaultdict # used to create dictionaries of lists


sitemap = ''
source = ''
soup = ''
firstels = defaultdict(list)    # used to iterate through soup 
output_dict = defaultdict(lambda: defaultdict(list)) # saves strings to get elements based on firstels
result_dict = defaultdict(list)
startUrl = ''