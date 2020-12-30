# can literally copy paste this to create any class

import DataExtraction
import config

class SelectorText(DataExtraction.DataExtraction):  # class extends DataExtractions
    
    def get_elements(self): # gets elements using prev defined strings, converts to scrapable code
        for selector in config.output_dict:
            if(selector == 'SelectorText'):
                y = 0
                for id in config.output_dict[selector]:
                    #print(id)
                    for x in range(len(config.output_dict[selector][id])):
                        config.output_dict[selector][id][x] += '.text'  # edit '.text' based on whichever Selectortype class its in
                        #print(config.output_dict[selector][id][x])
                    #print(config.output_dict[selector][id])
                    for string in config.output_dict[selector][id]:
                        #print(string)
                        #print(y)
                        #print(config.firstels[selector][y])
                        for item in config.soup.find_all(class_ = config.firstels[selector][y]):
                            #print(item)
                            #print(string)
                            result = eval(string)
                            config.result_dict[id].append(result)
                            #print(result)
                        y = y + 1
        
    