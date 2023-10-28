from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from models.reviews import Review

chromeOptions = Options()
# options.headless = True
chromeOptions.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")
# chromeOptions.add_argument("--headless=new")
chromeOptions.add_argument("--remote-debugging-port=9222")

chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=./cookies/test")
driver = webdriver.Chrome("./chromedriver", chrome_options=chromeOptions)

driver.get(
    "https://play.google.com/store/apps/details?id=com.sraoss.dmrc&hl=en_IN&gl=US"
)
time.sleep(5)

open_reviews_button = driver.find_element(
    By.XPATH,
    "/html/body/c-wiz[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/c-wiz[4]/section/div/div[2]/div[5]/div/div/button",
)

open_reviews_button.click()
time.sleep(2)

outer_div_for_reviews = driver.find_element(
    By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div[2]"
)
time.sleep(2)
review_set = set([])

with open("output.txt", "w") as file:
    review_divs = outer_div_for_reviews.find_elements(By.TAG_NAME, "div")
    try:
        for index, review_div in enumerate(review_divs):
            print(f"{index+1}", len(review_divs))
            if index != 0 and index % 40 == 0:
                driver.execute_script(
                    "arguments[0].scrollBy(0,12000);", outer_div_for_reviews
                )
                time.sleep(10)
            name = review_div.find_element(
                By.XPATH,
                f"/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[{index+1}]/header/div[1]/div[1]/div",
            ).text
            date_string = review_div.find_element(
                By.XPATH,
                f"/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[{index+1}]/header/div[2]/span",
            ).text
            rating_string = review_div.find_element(
                By.XPATH,
                f"/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[{index+1}]/header/div[2]/div",
            ).get_attribute("aria-label")

            review = review_div.find_element(
                By.XPATH,
                f"/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[{index+1}]/div[1]",
            ).text

            # print(name, review, date_string, rating_string)
            # review_set.add(Review(name, review, date_string, rating_string))
            file.write(f"\n{review}\n" if index % 10 == 0 else f"{review}\n")
    except:
        pass


"""
name => /html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/header/div[1]/div[1]/div
date => /html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/header/div[2]/span
rating=> /html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/header/div[2]/div
comment=> /html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]
"""
