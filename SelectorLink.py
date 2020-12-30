import DataExtraction
import config

class SelectorLink(DataExtraction.DataExtraction):
    
    def get_elements(self):
        for selector in config.output_dict:
            if(selector == 'SelectorLink'):
                y = 0
                for id in config.output_dict[selector]:
                    #print(id)
                    for x in range(len(config.output_dict[selector][id])):
                        config.output_dict[selector][id][x] += '[\'href\']'
                    for string in config.output_dict[selector][id]:
                        #print(string)
                        for item in config.soup.find_all(class_ = config.firstels[selector][y]):
                            #print(string)
                            result = eval(string)
                            config.result_dict[id].append(result)
                            #print(result)
                        y = y + 1
        
    
    