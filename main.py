from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
# options.headless = True
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--headless=new")
chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=./cookies/test") 
driver = webdriver.Chrome("./chromedriver", chrome_options=chromeOptions)
driver.get("https://www.geeksforgeeks.org/how-to-get-title-of-a-webpage-using-selenium-in-python/")
print(driver.title)
