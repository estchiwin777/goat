from .base import FunctionalTest

from unittest import skip
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  

from .base import FunctionalTest


# --- 4. คลาสทดสอบการตรวจสอบข้อมูล (Validation) ---
class ItemValidationTest(FunctionalTest):

    @skip  # บรรทัดนี้จะทำให้รันผ่านโดยขึ้นตัว 's'
    def test_cannot_add_empty_list_items(self):
        # โค้ดส่วนนี้ยังไม่สมบูรณ์ตามหนังสือ จึงต้องมีคำสั่งข้างใน
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        
        # ใส่คอมเมนต์อธิบายตามหนังสือได้ แต่ต้องมีคำสั่ง fail หรือ pass ข้างใน
        self.fail("write me!") #