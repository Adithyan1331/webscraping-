# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time

# # Setup Chrome Driver
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )

# # Open Flipkart
# url = "https://www.flipkart.com/search?q=perfume+under+1500"
# driver.get(url)

# # Wait for page to load
# time.sleep(5)

# # Scroll down a few times
# for _ in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# # Lists for storing data
# names = []
# prices = []
# ratings = []

# # Find products
# products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")

# print("Products Found:", len(products))

# for product in products:
#     try:
#         name = product.find_element(By.CSS_SELECTOR, "div.KzDlHZ").text
#     except:
#         name = "N/A"

#     try:
#         price = product.find_element(By.CSS_SELECTOR, "div.Nx9bqj").text
#     except:
#         price = "N/A"

#     try:
#         rating = product.find_element(By.CSS_SELECTOR, "div.XQDdHH").text
#     except:
#         rating = "No Rating"

#     names.append(name)
#     prices.append(price)
#     ratings.append(rating)

# # Create DataFrame
# df = pd.DataFrame({
#     "Product Name": names,
#     "Price": prices,
#     "Rating": ratings
# })

# # Save CSV
# csv_file = "flipkart_perfumes_under_1500.csv"
# df.to_csv(csv_file, index=False, encoding="utf-8-sig")

# print(f"\nSaved {len(df)} products to {csv_file}")
# print(df.head())

# driver.quit() 
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time

# # Setup Chrome Driver
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )

# # Open Flipkart
# url = "https://www.flipkart.com/search?q=perfume+under+1500"
# driver.get(url)

# # Wait for page to load
# time.sleep(5)

# # Scroll down a few times
# for _ in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# # Lists for storing data
# names = []
# prices = []
# ratings = []

# # Find products
# products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")

# print("Products Found:", len(products))

# for product in products:
#     try:
#         name = product.find_element(By.CSS_SELECTOR, "div.KzDlHZ").text
#     except:
#         name = "N/A"

#     try:
#         price = product.find_element(By.CSS_SELECTOR, "div.Nx9bqj").text
#     except:
#         price = "N/A"

#     try:
#         rating = product.find_element(By.CSS_SELECTOR, "div.XQDdHH").text
#     except:
#         rating = "No Rating"

#     names.append(name)
#     prices.append(price)
#     ratings.append(rating)

# # Create DataFrame
# df = pd.DataFrame({
#     "Product Name": names,
#     "Price": prices,
#     "Rating": ratings
# })

# # Save CSV
# csv_file = "flipkart_perfumes_under_1500.csv"
# df.to_csv(csv_file, index=False, encoding="utf-8-sig")

# print(f"\nSaved {len(df)} products to {csv_file}")
# print(df.head())

# driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.flipkart.com/search?q=perfume+under+1500")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-id]"))
)

products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")

print("Products Found:", len(products))

for p in products[:5]:
    print(p.text)
    print("=" * 50)

driver.quit()