from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Specify the path to your ChromeDriver
chrome_driver_path = r'C:\Users\mohan\chromedriver.exe'  # Update this to your actual path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the YouTube video page
url = 'https://www.youtube.com/watch?v=0cIT-CZ5Rxc'  # The specified video URL
driver.get(url)

# Wait for the page to load and comments to be present
try:
    # Wait for the comments section to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ytd-comment-thread-renderer'))
    )
except Exception as e:
    print(f"Error waiting for comments: {e}")
    driver.quit()

# Scroll down to load more comments if necessary
for _ in range(3):  # Adjust the range for more scrolling
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)  # Wait for comments to load

# Extract comments and usernames
comments_data = []
comments = driver.find_elements(By.XPATH, '//ytd-comment-thread-renderer')

for comment in comments:
    try:
        username = comment.find_element(By.XPATH, './/span[@class="style-scope ytd-comment-renderer"]').text
        comment_text = comment.find_element(By.XPATH, './/span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"]').text
        comments_data.append({'Username': username, 'Comment': comment_text})
    except Exception as e:
        print(f"Error extracting comment: {e}")

# Close the driver
driver.quit()

# Create a DataFrame
df = pd.DataFrame(comments_data)

# Perform basic analysis
print(f"Total comments scraped: {len(df)}")
print(df.head())  # Display the first few comments

# Save to CSV
df.to_csv('youtube_comments_analysis.csv', index=False)
print("Comments have been saved to 'youtube_comments_analysis.csv'")