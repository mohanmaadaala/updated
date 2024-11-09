from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment this line to run headless if needed

chrome_service = Service(executable_path=r"C:\Users\mohan\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL to scrape (starting URL for the first page)
url = "https://www.dice.com/jobs?q=certified%20ethical%20hacker%20instructor&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&utm_source=google&utm_medium=paid_search&utm_campaign=B2C_Brand_General&utm_term=dice%20technical&utm_content=70736557887&gclid=CjwKCAjw3624BhBAEiwAkxgTOiqaxMWdjlHFUPt_Wl4M-uLlSlRs1L4BlGCNVe_Xfe1WR6gOfqo5VBoCgisQAvD_BwE"
driver.get(url)

# Initialize a list to hold all job data across pages
all_jobs = []

# Function to scrape job cards from the current page
def scrape_jobs():
    job_cards = driver.find_elements(By.CSS_SELECTOR, 'div.card')
    for job in job_cards:
        try:
            title = job.find_element(By.CSS_SELECTOR, 'h5 a').text
            company = job.find_element(By.CSS_SELECTOR, 'a[data-cy="search-result-company-name"]').text
            location = job.find_element(By.CSS_SELECTOR, 'span[data-cy="search-result-location"]').text
            job_type = job.find_element(By.CSS_SELECTOR, 'span[data-cy="search-result-employment-type"]').text

            # Append job data to the list
            all_jobs.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Job Type': job_type
            })
        except Exception as e:
            print(f"Error scraping a job: {str(e)}")

# Scrape job postings from all pages
while True:
    try:
        # Wait for job cards to load
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card')))
        
        # Scrape jobs from the current page
        scrape_jobs()

        # Find the pagination bar and next button
        pagination = driver.find_element(By.CSS_SELECTOR, 'ul.pagination')
        next_button = pagination.find_element(By.CSS_SELECTOR, 'li.pagination-next a.page-link')

        # If the 'Next' button is present and enabled, click it
        if next_button:
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(3)  # Pause to allow the next page to load
            print("Moving to the next page...")

        else:
            print("Reached the last page or no next button found.")
            break

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        break

# Create a DataFrame from the scraped job data and save it to an Excel file
if all_jobs:
    df = pd.DataFrame(all_jobs)
    df.to_excel('dice_data_scientist_jobs.xlsx', index=False)
    print("Data successfully saved to dice_data_scientist_jobs.xlsx")
else:
    print("No job data found.")

# Clean up and close the browser
driver.quit()
