import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://ieeexplore.ieee.org")

# Accept cookies
try:
    accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_btn.click()
except:
    pass

# Search
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))
search_box.send_keys("AI for climate change weather forecasting")
search_box.submit()

# Wait for results page
wait.until(EC.url_contains("search"))

# Wait for results
results = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3 a"))
)

paper_links = []

for r in results:
    link = r.get_attribute("href")
    if link:
        paper_links.append(link)

# Save
df = pd.DataFrame({"Link": paper_links})
df.to_csv("ieee_links.csv", index=False)

print("✅ Links saved successfully")

driver.quit()