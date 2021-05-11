from bs4 import BeautifulSoup
import requests 
import pandas
page = requests.get("https://en.wikipedia.org/wiki/List_of_Category_5_Atlantic_hurricanes").content
soup = BeautifulSoup(page, 'lxml')
table = soup.find("table", {"class", "wikitable sortable"})
headers = [h.get_text(separator="\n") for h in table.find_all('th')][:-2]
#print(headers)

table_info = []
for row_info in table.find_all("tr"):
	entries = row_info.find_all("td")
	row_values = [entry.text.strip() for entry in entries][:-1]
	if(len(row_values) > 0): 
		#print(row_values)
		table_info.append(row_values)

dataframe = pandas.DataFrame(table_info, columns = headers)
dataframe.to_csv('finished.csv')