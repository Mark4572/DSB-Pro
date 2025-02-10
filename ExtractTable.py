import requests
import pandas as pd

from bs4 import BeautifulSoup


# Fetch the HTML content

url = 'https://light.dsbcontrol.de/DSBlightWebsite/Data/86d013b9-c2de-4644-bdf6-43a413038ad1/68855201-6c03-4d33-914e-b064bb8ddd7b/V_DC_001.html'

response = requests.get(url)

response.raise_for_status()  # Check if the request was successful

soup = BeautifulSoup(response.content, 'html.parser')


# Find the table and read it into a DataFrame

table = soup.find('table')

def print_dataframe(df):
    print(df)


if table is not None:

    df = pd.read_html(str(table))[0]


    # Display the DataFrame
    print_dataframe(df)
    

    # Convert the DataFrame to JSON and save it to Data.json

    json_data = df.to_json(orient='records', lines=True)

    with open('Data.json', 'w') as f:
        f.write(json_data)

else:

    print("No table found in the HTML content")


txt = str (json_data)


txt.replace("\u00e4", "ä")


print(txt)

