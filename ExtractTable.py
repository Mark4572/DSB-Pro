import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_and_process_table(url, output_file):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table and read it into a DataFrame
    table = soup.find('table')
    if table is not None:
        df = pd.read_html(str(table))[0]

        # Display the DataFrame
        print(df)

        # Convert the DataFrame to JSON and save it to the specified file
        json_data = df.to_json(orient='records', lines=True)
        with open(output_file, 'w') as f:
            f.write(json_data)
    else:
        print(f"No table found in the HTML content of {url}")

# First URL
url1 = 'https://dsbmobile.de/data/86d013b9-c2de-4644-bdf6-43a413038ad1/b1b3402b-b0f5-46ad-8b97-78b7226f8199/V_DC_001.html'
fetch_and_process_table(url1, '/Data1.json')

# Second URL
url2 = 'https://dsbmobile.de/data/86d013b9-c2de-4644-bdf6-43a413038ad1/b1b3402b-b0f5-46ad-8b97-78b7226f8199/V_DC_002.html'
fetch_and_process_table(url2, '/Data2.json')