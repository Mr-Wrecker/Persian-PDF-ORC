import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ._CONST import Image_Directory, Default_Link
from .download import downloader

URL = "https://www.i2ocr.com/free-online-persian-ocr"
delayTime = 2

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")


def Custom_Sleep(*args):
    if not args:
        time.sleep(delayTime)

    else:
        while True:
            time.sleep(delayTime)
            if args[0].find_element(args[1], args[2]):
                break


def OCR():
    # Create Driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

    # Load Page
    driver.get(URL)
    Custom_Sleep()

    images = []
    IMG_PATH = os.path.join(os.getcwd(), Image_Directory)
    # Iterate directory
    for path in os.listdir(os.path.join(IMG_PATH)):
        # check if current path is a file
        if os.path.isfile(os.path.join(IMG_PATH, path)):
            images.append(f"{IMG_PATH}/{path}")
    print(images)

    # Upload Image File
    Btn = driver.find_element(By.XPATH, '//*[@id="i2ocr_uploadedfile"]')
    Custom_Sleep()
    Btn.send_keys(images[0])

    Custom_Sleep(
        driver,
        By.XPATH,
        '//*[@id="i2ocr_form"]/div[1]/div[2]/div[5]'
    )

    driver.find_element(By.XPATH, '//*[@id="submit_i2ocr"]').submit()

    while True:
        time.sleep(delayTime)
        if driver.find_element(By.ID, 'download_text').get_attribute('href') != Default_Link:
            break

    href = driver.find_element(By.ID, 'download_text').get_attribute('href')
    downloader(href)
