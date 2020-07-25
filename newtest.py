"""
Created on Sat Jul 25 2020

@author: Leron

"""
#import libraries
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

# pulling the html
#url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
#html = urllib.request.urlopen(url).read()

#dumping the html into a file
#with open('Table.txt','w') as File1:
#    File1.write(str(html))

#reading the HTML from file
with open('Table.txt','r') as File1:
    html = File1.read()

#parsing the data from the file
soup = BeautifulSoup(html,'html.parser')
#Retrieving data from the html
table = soup.find('table',attrs = { 'class' : 'wikitable sortable jquery-tablesorter'})
table_body = soup.find('tbody')
rows = table_body.find_all('tr')
#print(rows)

#list for each column
postal_code_list = []
borough_list = []
neighbourhood_list = []

#creating a function to extract the text from the List_op_rows
def text_extractor(ele):
    temp_str = ele.get_text()
    temp_lst = temp_str.replace('\\n','')
    return temp_lst
#print(temp_lst)
#printing elements from the table
for row in rows:
    line = row.find_all('td')
    counter_i = 0
    for ele in line:
        if counter_i == 0:
            postal_code_list.append(text_extractor(ele))
        elif counter_i == 1:
            borough_list.append(text_extractor(ele))
        elif counter_i == 2:
            neighbourhood_list.append(text_extractor(ele))
        else:
            pass
        counter_i = counter_i + 1

print(postal_code_list[0:5])
print(borough_list[0:5])
print(neighbourhood_list[0:5])

dict_df = {'Postal Code': postal_code_list,'Borough':borough_list,'Neighbourhoods':neighbourhood_list}


#converting dict to data frame
import pandas as pd
toronto_df = pd.DataFrame.from_dict(dict_df)

print(toronto_df.head())
print('---------------------------------------------')
print(toronto_df.info())
print('----------------------------------------------')
#publishing the DataFrame to csv 
toronto_df.to_csv('Toronto_postal_codes.csv')
