from selenium.webdriver.firefox.options import Options # บรรทัดนี้แหละที่หายไป!
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import os
from unittest import skip

MAX_WAIT = 5


# --- 1. Base Class (เครื่องมือส่วนกลาง) ---
class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertTrue(
                    any(row_text in row.text for row in rows)
                )
                return 
            except (AssertionError, WebDriverException, NoSuchElementException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row_text in row.text for row in rows)
        )