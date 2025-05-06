# 📞 **Dubizzle Contact Scrapper**
Python Script to extract contact info from Dubizzle ads using Selenium Webdriver. The extracted information is saved in a csv file.
This project automates the process of scraping contact details, such as phone numbers, from Dubizzle listings. It's particularly useful for real estate agents, marketers, or researchers seeking to gather contact information from property advertisements.

## ⚙️ **Features**
- Automated navigation through Dubizzle ads.
- Extraction of phone numbers.
- Export of collected data into a CSV file for easy analysis.
- Utilization of Selenium WebDriver for dynamic content handling.

## 🚀 **Installation**
1. Clone the repository:
```
git clone https://github.com/ayousaf21/Dubizzle-Contact-Scrapper.git
cd Dubizzle-Contact-Scrapper
```
2. Required Python 3.8 >=. Install required Python packages:
```
pip install -r requirements.txt
```
3. Download ChromeDriver:
Ensure that the version of ChromeDriver matches your installed version of Google Chrome.
Place the chromedriver.exe in the project directory or specify its path in the script.

## 🛠️ **Usage**
Run the script:
```
python driver.py
```

Follow the on-screen prompts:

- The script will open a Chrome window and navigate through the Dubizzle ads.
- It will extract contact information and save it to a CSV file named phone_numbers_{timestamp}.csv.
