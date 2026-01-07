import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # ใช้ที่อยู่แบบเต็ม (Absolute Path) เพื่อป้องกันปัญหาหาไฟล์ไม่เจอ
        base_path = os.path.dirname(os.path.abspath(__file__))
        firefox_bin = os.path.join(base_path, 'firefox', 'firefox')

        options = Options()
        options.binary_location = firefox_bin
        
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith เข้าหน้าแรกของแอป To-Do
        self.browser.get('http://localhost:8000')

        # เธอสังเกตว่าพาดหัว (header) และชื่อเว็บ (title) มีคำว่า To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element("tag name", "h1").text
        self.assertIn('To-Do', header_text)

        # เธอได้รับเชิญให้พิมพ์รายการ To-Do ทันที
        inputbox = self.browser.find_element("id", "id_new_item")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        import time

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        table = self.browser.find_element("id", "id_list_table")
        rows = table.find_elements("tag name", "tr")
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows],
        )
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows],
        )


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()