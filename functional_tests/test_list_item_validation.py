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
        
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
         # The home page refreshes, and there is an error message saying
    # that list items cannot be blank
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        # She tries again with some text for the item, which now works
        self.browser.find_element(By.ID, "id_new_item").send_keys("Purchase milk")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Purchase milk")

        # Perversely, she now decides to submit a second blank list item
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        # And she can correct it by filling some text in
        self.browser.find_element(By.ID, "id_new_item").send_keys("Make tea")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("2: Make tea")

        # ใส่คอมเมนต์อธิบายตามหนังสือได้ แต่ต้องมีคำสั่ง fail หรือ pass ข้างใน
        self.fail("write me!") #