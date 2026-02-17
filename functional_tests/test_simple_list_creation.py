from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

# --- 3. คลาสทดสอบสำหรับผู้เยี่ยมชมใหม่ ---
class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        prioritybox = self.browser.find_element(By.ID, 'id_item_priority')
        prioritybox.send_keys('High')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers (Priority: High)')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # โค้ดเดิมของคุณ (ขอย่อเพื่อความสั้น)
        self.browser.get(self.live_server_url)
        # ... (โค้ดทดสอบ 2 Users) ...

