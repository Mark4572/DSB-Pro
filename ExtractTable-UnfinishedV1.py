import requests
import pandas as pd
from bs4 import BeautifulSoup

# Fetch the HTML content
url = 'https://light.dsbcontrol.de/DSBlightWebsite/Data/86d013b9-c2de-4644-bdf6-43a413038ad1/7e204a37-0c66-4988-8110-9fa4dcfb346a/V_DC_001.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table and read it into a DataFrame
table = soup.find('table')
print(table)
df = pd.read_html(str(table))

# Display the DataFrame
print(df)
#df.to_csv('MyData.csv', index=False)