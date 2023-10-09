import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = "https://en.wikipedia.org/wiki/MS_Dhoni"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data you want to scrape (you'll need to inspect the Wikipedia page's HTML structure)
    # For example, let's assume you want to scrape the Infobox details.
    infobox = soup.find("table", {"class": "infobox"})

    # Define a dictionary to store the scraped data
    data = {}

    # Iterate through rows in the Infobox table
    for row in infobox.find_all("tr"):
        th = row.find("th")
        td = row.find("td")
        if th and td:
            data[th.text.strip()] = td.text.strip()

    # Define the CSV file name
    csv_file = 'ms_dhoni_data.csv'

    # Write the scraped data to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        # Create a CSV writer
        csv_writer = csv.writer(csvfile)

        # Write the data to the CSV file
        for key, value in data.items():
            csv_writer.writerow([key, value])

    print(f"Scraped data saved to {csv_file}")
else:
    print("Failed to retrieve data from the Wikipedia page.")






