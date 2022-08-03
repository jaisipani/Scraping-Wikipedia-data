'''
Requirement.txt: use python3
install beautifulsoup using pip: pip install beautifulsoup4
install requests using pip install requests
'''

import requests 
import urllib.request
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

'''
arguement: url from where the data has to be fethed
return: dictionary who keys are the table headers and values are list of data for that particular column header

'''
def getData(url):
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('table' , class_='wikitable')
    trs = tables[0].find_all('tr')

    ths = trs[0]
    trs = trs[1:]


    data_dic = {}

    university = []
    tpe = []
    campus = []
    state = []
    established = []
    uni_status = []

    for tr in trs:

        tds = tr.find_all('td')

        university.append(tds[0].text)
        tpe.append(tds[1].text)
        campus.append(tds[2].text)
        state.append(tds[3].text)
        established.append(tds[4].text)
        uni_status.append(tds[5].text)

    data_dic['university'] = university
    data_dic['Type'] = tpe
    data_dic['Campus'] = campus
    data_dic['State'] = state
    data_dic['Established'] = established   
    data_dic['University_Status'] = uni_status 

    return data_dic

with open('./input/url.txt') as f:
    url = f.read()
    print(url)
    
url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Australia'
data_dic = getData(url)


uni_details = ['University' , 'Type', 'Campus', 'State', 'Established', 'University_status']

# Wrting the data into csv file
with open('test.csv' , 'w')  as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(uni_details)
    for i in range(0, len(data_dic['university'])):
        writer.writerow([data_dic['university'][i],data_dic['Type'][i],data_dic['Campus'][i],data_dic['State'][i],data_dic['Established'][i],data_dic['University_Status'][i]])
