import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ._CONST import Images_Path, Default_Link, OCR_Path
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
            # Driver, Find_Element_Method, Value
            if len(args) == 3 and args[0].find_element(args[1], args[2]):
                break

            # Driver, Find_Element_Method, Value, Condition
            elif len(args) == 4 and args[0].find_element(args[1], args[2]) != args[3]:
                break

            # Driver, Find_Element_Method, Value, Condition, href
            elif len(args) == 5 and args[0].find_element(args[1], args[2]).get_attribute('href') != args[3]:
                break


def OCR():
    # Create Driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

    # Load Page
    driver.get(URL)
    Custom_Sleep()

    images = []
    # Iterate directory
    for path in os.listdir(Images_Path):
        # check if current path is a file
        if os.path.isfile(os.path.join(Images_Path, path)):
            images.append(f"{Images_Path}/{path}")

    images = sorted(images)

    State = None
    Link = Default_Link
    # Upload Image File
    for img in images:
        img_name = img.split('/')[-1][:-4]
        print(f"\nProcess For {img_name}")

        # Skip Exist Process
        if os.path.exists(f"{OCR_Path}/{img_name}.docx"):
            print('Result is Exist.')
            continue

        # Find Select Image Button and Upload Image
        Btn = driver.find_element(By.XPATH, '//*[@id="i2ocr_uploadedfile"]')
        Custom_Sleep()
        Btn.send_keys(img)

        Custom_Sleep(
            driver,
            By.XPATH,
            '//*[@id="i2ocr_form"]/div[1]/div[2]/div[5]'
        )

        # Set State
        State = driver.find_element(
            By.XPATH, '//*[@id="filestat"]').text
        Custom_Sleep(
            driver,
            By.XPATH,
            '//*[@id="filestat"]',
            State
        )

        # Extract Text
        driver.find_element(By.XPATH, '//*[@id="submit_i2ocr"]').submit()
        Custom_Sleep(
            driver,
            By.ID,
            'download_docx_box',    # download_text, download_docx_box, download_docx_section
            Link,
            'href'
        )

        # Find Link of Result And Download
        href = driver.find_element(
            By.ID, 'download_docx_box').get_attribute('href')
        Link = href
        downloader(href, img_name)
