import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from openpyxl import Workbook

# Set up the Chrome driver using Service
chrome_service = Service('C:\\Users\\mohan\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)

# Open the target website
driver.get('https://ceoaperolls.ap.gov.in/AP_MLC_2024/ERO/Status_Update_2024/knowYourApplicationStatus.aspx')

# Increase waiting time to 20 seconds
wait = WebDriverWait(driver, 20)

# Wait for the Graduate tab to load and click it
graduate_tab = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-item.nav-link[href="#Graduate"]'))
)
print("Graduate tab clicked.")
graduate_tab.click()

# Select Application ID radio button
application_id_radio = wait.until(
    EC.element_to_be_clickable((By.ID, 'GraduateAppID'))
)
application_id_radio.click()
print("Application ID radio button selected.")

# Define the path to save the Excel file
file_path = os.path.join(os.getcwd(), 'applications.xlsx')

# Create a new Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active
sheet.title = "Application Data"

# Write the header row in Excel
sheet.append(["App ID", "PS_NO", "SLNO", "Name", "Relation Name", "House Number", "Age", "AERO Comments", "Ero Comments", "App Status"])

# Search for Application IDs between F18-0000001 and F18-0000010
for app_id in range(1, 11):
    app_id_str = f'F18-{app_id:07d}'
    print(f"Searching for Application ID: {app_id_str}")
    
    # Enter the Application ID in the search field
    search_box = driver.find_element(By.ID, 'TextBox2')
    search_box.clear()
    search_box.send_keys(app_id_str)
    
    # Click the "Search" button
    search_button = driver.find_element(By.ID, 'btnGraduates')
    search_button.click()
    
    # Wait for the results table to load
    try:
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        print(f"Data fetched for Application ID: {app_id_str}")
    except:
        print(f"No data found for Application ID: {app_id_str}")
        continue
    
    # Extract the data from the table
    rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        if columns:
            app_data = [col.text for col in columns]
            print(f"Writing data to Excel: {app_data}")
            sheet.append(app_data)
    
    # Wait for a short time before moving to the next Application ID
    time.sleep(2)

# Save the Excel file
workbook.save(file_path)

# Close the browser
driver.quit()

print(f"Data saved successfully to {file_path}")
