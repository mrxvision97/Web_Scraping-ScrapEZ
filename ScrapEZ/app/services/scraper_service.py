import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all table elements on the page
    tables = soup.find_all("table")

    data_frames = []

    # Loop through each table and extract data
    for table in tables:
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")

        # Extract column names
        columns = []
        for th in table_body.find_all("th"):
            columns.append(th.text.strip())

        # Extract row data
        data = []
        for row in rows:
            row_data = []
            for td in row.find_all("td"):
                row_data.append(td.text.strip())
            data.append(row_data)

        # Create a DataFrame from the table data
        table_df = pd.DataFrame(data, columns=columns)
        data_frames.append(table_df)

    # Concatenate all DataFrames into one
    data = pd.concat(data_frames, ignore_index=True)

    return data