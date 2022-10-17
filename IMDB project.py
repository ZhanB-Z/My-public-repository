from bs4    import  BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://www.imdb.com/chart/top/?ref_=login'
html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

#table_col = soup.find_all('td')
#print(table_col)
#table_row = soup.find_all('tr')
#print(table_row[0])

imdb_data = pd.DataFrame(columns=["Rank and Title", "Rating", "Title","Year"])
#print(imdb_data)



for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    RaT = str(col[1].text).strip().replace('\n','') # used str.strip() to get rid of the '\n' characters
    rating = str(col[2].text).strip()
    imdb_data = imdb_data.append(
        {"Rank and Title": RaT, "Rating": rating}, ignore_index=True)

b = []
i = 0
while i < len(imdb_data):
    b = ' '.join(imdb_data['Rank and Title'][i].split()[1:])
    title = b[:-6]
    year = b[-5:-1]
    #print(b)
    #the below part doesn't work

    imdb_data.iloc[i, imdb_data.columns.get_loc('Title')] = title
    imdb_data.iloc[i, imdb_data.columns.get_loc('Year')] = year
    i = i + 1


#imdb_data['Year'] = b[-5:-1]
print(imdb_data)

del imdb_data["Rank and Title"]
print(imdb_data)

imdb_data.to_csv(r'C:\Users\Zhan\Desktop\Coding\IMDB.csv')

print('Done')


