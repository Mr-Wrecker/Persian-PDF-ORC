import time
from selenium.webdriver.common.by import By

audioToTextDelay = 10
GoogleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'


def saveFile(content, filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)


def audioToText(driver, mp3Path):
    print("Try To Bypass With speech-to-text...")

    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    print("Switched To Site Window")

    driver.get(GoogleIBMLink)
    delayTime = 10
    time.sleep(1)
    print("Load Site")

    # Upload file
    time.sleep(1)
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    # path
    btn.send_keys(mp3Path)
    # Audio to text is processing
    time.sleep(delayTime)
    # btn.send_keys(path)
    print("Send MP3 File To Site")

    # Audio to text is processing
    time.sleep(audioToTextDelay)
    text = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements(By.TAG_NAME, 'span')
    print("Reading Text")

    result = " ".join([each.text for each in text])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Return Result")
    return result
