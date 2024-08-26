
import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rhinoinsight.substack.com/archive") #URL of the Substack you want to scrap

# Step 2: Scroll to the bottom to load more posts
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for new posts to load
    time.sleep(3)  # adjust this as needed, depending on your internet speed
    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Step 3: After loading all posts, parse the page content
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Step 4: Extract article titles, subtitles, and links
articles = []

# Find the portable-archive-list container
archive_list = soup.find('div', class_='portable-archive-list')
if archive_list:
    # Extract all the titles, subtitles, and links
    title_elements = archive_list.find_all('a', attrs={"data-testid": "post-preview-title"})
    subtitle_elements = archive_list.find_all('a', class_="_color-primary_3axfk_183")

    for title_elem, subtitle_elem in zip(title_elements, subtitle_elements):
        title = title_elem.text.strip()
        subtitle = subtitle_elem.text.strip()
        link = title_elem['href']

        # Append the extracted data to the articles list
        articles.append({
            "Title": title,
            "Subtitle": subtitle,
            "Link": link
        })

# Step 5: Store the data in an Excel file
df = pd.DataFrame(articles)
df.to_excel("substack_articles_with_links.xlsx", index=False, engine='openpyxl')
print("Data successfully written to substack_articles_with_links.xlsx")
