import os
import sys
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InformationGetter:
    def __init__(self, download_path: str, driver_path: str):
        self.download_path = download_path
        self.driver_path = driver_path

    def downloader(self):
        options = Options()
        options.headless = True
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", str(sys.argv[1]))
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

        service = Service(executable_path=self.driver_path)
        driver = webdriver.Firefox(service=service, options=options)

        driver.get(
            "https://www.chathamfinancial.com/technology/us-forward-curves")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-js-hook="rates-download"]')))
        element.click()
        time.sleep(10)
        driver.quit()

    def rename(self):
        name = os.listdir(sys.argv[1])[0]
        os.rename(sys.argv[1] + '/' + name, sys.argv[1] + '/file.xlsx')

    def reader(self):
        df = pd.read_excel('./download/file.xlsx')
        df = df[['Unnamed: 14', 'Unnamed: 15']]
        return df


if __name__ == '__main__':
    getter = InformationGetter(sys.argv[1], sys.argv[2])
    getter.downloader()
    getter.rename()
    print(getter.reader())
