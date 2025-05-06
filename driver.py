from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

#####################################################################
#####################################################################
LIMIT = 10
#####################################################################
#####################################################################

base_url = "https://dubai.dubizzle.com"
path = "/en/property-for-sale/residential/apartment/"
page = 1
url = base_url + path + "?page=" + str(page)

print(url)

count = 1

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
service = Service("chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(3)

driver.get(url)
time.sleep(10)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"phone_numbers_{timestamp}.csv"

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Listing Number", "Phone Number"])
    while not page > LIMIT:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-7b1bceda-0"))
        )

        call_buttons = driver.find_elements(
            By.CSS_SELECTOR, 'button[data-testid="call-cta-button"]'
        )

        for index, call_button in enumerate(call_buttons):
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(call_button))
                call_button.click()

                time.sleep(3)

                soup = BeautifulSoup(driver.page_source, "html.parser")
                popup = soup.find("div", class_="MuiDialog-paper")
            except:
                continue

            if popup:
                try:
                    phone_number = popup.find(
                        "h6", {"data-testid": "phone-number"}
                    ).text

                    writer.writerow([index + 1, phone_number])
                    print(f"Listing {index + 1}: Phone Number: {phone_number}")
                except:
                    continue
            else:
                print(f"Listing {index + 1}: Popup not found")

            time.sleep(1)

            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            time.sleep(1)
            count += 1
            if count == 3:
                webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                time.sleep(1)

        print(f"------ Page {page} Completed -------- ")
        page += 1

        try:
            next_button = driver.find_element(
                By.CSS_SELECTOR, 'a[data-testid="page-next"]'
            )
            next_button.click()
            time.sleep(3)
        except Exception as e:
            print("No more pages or could not find next button.")
            break


driver.quit()
