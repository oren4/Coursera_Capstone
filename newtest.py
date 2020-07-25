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

with open('Table.txt','r') as File1:
    html = File1.read()

soup = BeautifulSoup(html,'html.parser')

#Retrieving data from the html
table = soup.find('table',attrs = { 'class' : 'wikitable sortable jquery-tablesorter'})
table_body = soup.find('tbody')
rows = table_body.find_all('tr')
#print(rows)
for row in rows:
    line = row.find_all('td')
    for ele in line:
        temp_str = ele.get_text()
        temp_lst = temp_str.replace('\\n','')
        print(temp_lst)
