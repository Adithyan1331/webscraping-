from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configure Chrome
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Flipkart search URL
url = "https://www.flipkart.com/search?q=smartphones+under+20000"
driver.get(url)

# Wait for page to load
time.sleep(5)

phones = []

# Get product cards
products = driver.find_elements(By.CSS_SELECTOR, "div.tUxRFH")

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, "div.KzDlHZ").text
        price = product.find_element(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR").text

        phones.append({
            "Phone Name": name,
            "Price": price
        })

    except Exception:
        continue

driver.quit()

# Save to Excel
df = pd.DataFrame(phones)

df.to_excel("flipkart_smartphones_under_20000.xlsx", index=False)

print(df)
print("\nData saved to flipkart_smartphones_under_20000.xlsx")