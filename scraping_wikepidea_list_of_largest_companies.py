from bs4 import BeautifulSoup
import requests 

page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
soup = BeautifulSoup(page.text , "html.parser")   

table = soup.find_all('table')[0]
columns_list = table.find_all('th')
columns_table=[column.text.strip() for column in columns_list]




import pandas as pd
df = pd.DataFrame(columns = columns_table)

row_tr = table.find_all('tr')
for row in row_tr :
  row_td = row.find_all('td')
  each_row_list = [element.text.strip() for element in row_td]
  
  if each_row_list :
    lenght = len(df) 
    df.loc[lenght] = each_row_list

print(df)