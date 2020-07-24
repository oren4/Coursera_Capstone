"""
Created on Thu Jul 27 2020

@author: Leron
"""

#import libraries
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

# pulling the html
url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieving data from the html
table = soup.find('table',attrs = { 'class' : 'wikitable sortable jquery-tablesorter'})
table_body = soup.find('tbody')
rows = table_body.find_all('tr')
#print('These are rows',rows)
for row in rows:
    row1 = row.find('td')
    print(row1.td.get_text())
#print(soup.tr.get_text())

#with open('Table.txt','w') as File1:
#    for row in rows:
#        File1.write(str(row))


#now we create dictionaries for the data from the table
postal_code = []
borough = []
neighbourhood = []
dict_df = {'Postal Code': postal_code, 'Borough': borough, 'Neighbourhoods': neighbourhood}

List_op_rows = []

#for row in rows:
#    List_op_rows.append(row.find_all('tr'))

    #for i in range(1):
    #    postal_code.append(row.find('td'))
    #    borough.append(row.find('td'))
    #    neighbourhood.append(row.find('td'))
#print(List_op_rows)
