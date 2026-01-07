from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # ถ้าพังตรงนี้ ให้เปลี่ยนเป็น webdriver.Firefox() หรือใช้ webdriver-manager
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_input_title_and_body(self): # <--- เช็คชื่อตรงนี้
        # 1. เข้าหน้าเว็บ
        self.browser.get('http://localhost:8000')

        # 2. เช็ค Title
        self.assertIn('Hello', self.browser.title)

        # 3. ลองกรอกข้อมูล
        body_box = self.browser.find_element(By.ID, 'id_body')

        body_box.send_keys('Sawadee by Singhanat Portongkam' )
        
        time.sleep(1) # หยุดดูผลลัพธ์ 2 วินาที
        
    
    

if __name__ == '__main__':
    unittest.main()