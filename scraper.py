from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

!git clone https://github.com/procodingclass/PRO-Stars-Dataset-CSVs

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Sethttps://www.selenium.dev/documentation/up/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

bright_stars = pd.read_csv('/procodingclass/PRO-Stars-Dataset-CSVs/blob/main/bright_stars.csv')
dwarf_stars = pd.read_csv('/procodingclass/PRO-Stars-Dataset-CSVs/blob/main/dwarf_stars.csv')

bright_stars.head()
dwarf_stars.head()

bright_stars.drop(columns=['NaN'], inplace=True)

final_planet_df = pd.merge(bright_stars,dwarf_stars)

final_planet_df.head()

final_planet_df.shape
final_planet_df.to_csv('bright_stars.csv','dwarf_stars.csv')

final_planet_df.tail(10)

time.sleep(10)

planets_data = []
scraped_data=[]

def scrape():
    print(hyperlink)
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")

        new_planets_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

    
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")


bright_star_table=soup.find("table",attrs={"class","wikitable"})
table_body=bright_star_table.find('tbody')
table_rows=table_body.find_all('tr')

for row in table_rows:
    table_cols=row.find_all('td')
    temp_list=[]
    print(table_cols)
    for col_data in table_cols:
        print(col_data.text)
        data=col_data.text.strip()
        print(data)
        temp_list.append(data)
        scraped_data.append(temp_list)

for i in range(0,len(scraped_data)):
    Star_names=scraped_data[i][1]
    Distance=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]
    Lum=scraped_data[i][7]

    required_data=[Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

headers=['Star_name','Distance','Mass','Radius',"Luminosity"]
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True,index_label='id')
planet_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")