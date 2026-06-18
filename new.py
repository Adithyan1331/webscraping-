import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. Initialize Chrome Driver securely using webdriver-manager
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless") # Uncomment to run without opening a browser window

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 2. Target URL
url = "https://www.flipkart.com/search?q=phone+under+15000"
driver.get(url)

# Wait for the page content to load fully
time.sleep(5)

# Container for all search product cards (div with data-id is stable)
products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
print(f"Products found: {len(products)}")

# 3. Helper Functions for robust scraping
def get_name(product):
    try:
        # Check standard layout title classes
        return product.find_element(By.CSS_SELECTOR, "div.KzDlHZ, div._4rR01T, div.RG5Slk").text
    except:
        try:
            # Fallback 1: Try getting the alt text of the product image (highly stable fallback)
            return product.find_element(By.CSS_SELECTOR, "img").get_attribute("alt")
        except:
            try:
                # Fallback 2: Grab text inside any anchor link within the card
                return product.find_element(By.TAG_NAME, "a").text
            except:
                return "N/A"

def get_rating(product):
    try:
        return product.find_element(By.CSS_SELECTOR, "div.XQD0w-, div._3LWZlK, div.MKiFS6").text
    except:
        return "N/A"

def get_price(product):
    try:
        return product.find_element(By.CSS_SELECTOR, "div.Nx9w7M, div._30jeq3, .hZ3P6w").text
    except:
        return "N/A"

def get_reviews(product):
    try:
        return product.find_element(By.CSS_SELECTOR, "span.Wphh3N, span._2_R_DZ, span.PvbNMB").text
    except:
        return "N/A"


# 4. Open CSV file and write scraped data
with open("new.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Mobile Name", "Price", "Rating", "Reviews"])

    for product in products:
        # Extract fields using the helper functions
        name = get_name(product).strip().replace("\n", " ")
        price = get_price(product).strip()
        rating = get_rating(product).strip()
        reviews = get_reviews(product).strip()

        # Save valid entries to prevent blank rows
        if name != "N/A" or price != "N/A":
            writer.writerow([name, price, rating, reviews])
            print(f"Scraped: {name} | {price} | {rating} | {reviews}")

# Close the browser session
driver.quit()
print("\nCSV Created Successfully!")