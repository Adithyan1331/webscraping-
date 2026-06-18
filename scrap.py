import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# URL of the Travel category
url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# Send GET request
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Save book titles to CSV
    csv_file = "travel_books.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["Book Title"])

        # Extract and save titles
        for book in soup.find_all("h3"):
            title = book.find("a")["title"]
            writer.writerow([title])

    print(f"Travel book titles have been saved to {csv_file}")

    # Read CSV and convert to Excel
    df = pd.read_csv(csv_file)
    excel_file = "travel_books.xlsx"
    df.to_excel(excel_file, index=False)

    print(f"CSV file converted to Excel and saved as {excel_file}")

else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")