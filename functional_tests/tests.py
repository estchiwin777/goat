from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        # ใช้ path ที่เราเช็คแล้วว่าเป็นทางลัดไปสู่ snap
        options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()
    
    # แก้ไขฟังก์ชันนี้ให้ "รอ" อัตโนมัติ
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return 
            except (AssertionError, WebDriverException, NoSuchElementException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_layout_and_styling(self):
        # ผู้ใช้เข้าหน้าโฮมเพจ
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # เธอสังเกตว่าช่องกรอกข้อความถูกจัดวางไว้ตรงกลางอย่างสวยงาม
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=30
        )

        # เธอเริ่มลิสต์ใหม่และพบว่าช่องกรอกในหน้าถัดไป (หน้า List) ก็อยู่ตรงกลางด้วย
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        
        # ต้องรอให้หน้าโหลดและแสดงตารางก่อน (ฟังก์ชันรอที่คุณมีอยู่แล้ว)
        self.wait_for_row_in_list_table('1: testing (Priority: Medium)')
        
        # หาช่องกรอกใหม่อีกครั้งในหน้า List
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=30
        )

    def test_can_start_a_list_for_one_user_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

        # 1. กรอกข้อความ
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')

        # 2. เลือก Priority (สมมติว่าเป็น Dropdown ที่มี ID ว่า id_item_priority)
        prioritybox = self.browser.find_element(By.ID, 'id_item_priority')
        prioritybox.send_keys('High') # หรือเลือกตาม value เช่น 'H'

        # 3. กด Enter
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # ตรวจสอบว่าบรรทัดที่เพิ่ม มีทั้งข้อความและ Priority
        self.check_for_row_in_list_table('1: Buy peacock feathers (Priority: High)')

    def test_default_priority_is_medium(self):
        self.browser.get(self.live_server_url)

        # กรอกแค่ข้อความ ไม่ต้องไปยุ่งกับ Dropdown Priority
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # ตรวจสอบว่าระบบใส่ (Priority: Medium) ให้เองโดยอัตโนมัติ
        self.check_for_row_in_list_table('1: Buy milk (Priority: Medium)')

    #ตรวจสอบให้แน่ใจว่า Priority ของรายการใน List หนึ่ง จะไม่ไปโผล่ผิดที่ในอีก List หนึ่ง
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # ผู้ใช้คนที่ 1 เริ่มลิสต์ใหม่
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Item 1 High')
        
        # เลือก High
        prioritybox = self.browser.find_element(By.ID, 'id_item_priority')
        prioritybox.send_keys('High')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        user_1_url = self.browser.current_url
        self.assertRegex(user_1_url, '/lists/.+')
        self.browser.quit()

        # ผู้ใช้คนที่ 2 เข้ามา (เปิดเบราว์เซอร์ใหม่หรือเคลียร์คุกกี้)
        options = Options()
        options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'
        self.browser = webdriver.Firefox(options=options)
        self.browser.get(self.live_server_url)
        
        # หน้าแรกต้องไม่มีรายการของคนที่ 1
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Item 1 High', page_text)
        

        # คนที่ 2 เพิ่มรายการแบบ Low
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Item 2 Low')
        prioritybox = self.browser.find_element(By.ID, 'id_item_priority')
        prioritybox.send_keys('Low')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # คนที่ 2 ต้องเห็นแค่รายการของตัวเอง
        self.check_for_row_in_list_table('1: Item 2 Low (Priority: Low)')
        self.assertNotIn('Item 1 High', self.browser.find_element(By.TAG_NAME, 'body').text)