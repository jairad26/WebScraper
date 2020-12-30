import DataExtraction
import SelectorText
import SelectorLink
import config
import csv
import sys



def writeToCSV():
    csvList = []
    for header in config.result_dict:
        list = []
        list.append(header)
        for item in config.result_dict[header]:
            item2 = item.strip()
            list.append(item2)
        csvList.append(list)
    #print(csvList)
    f = open('sitemap_data_rows.csv', 'w', newline ='')
    with f:
        write = csv.writer(f)
        write.writerows(csvList)
    f.close()    
        
        
def main():
    #file = input("Enter sitemap file name: ")
    #DataExtraction.DataExtraction.create_extraction_elements(DataExtraction, file)

    
    DataExtraction.DataExtraction.create_extraction_elements(DataExtraction, sys.argv[1])
    
    SelectorText.SelectorText.get_elements(SelectorText)
    SelectorLink.SelectorLink.get_elements(SelectorLink)
    writeToCSV()
    
   
        
    
if __name__ == "__main__":
    main()