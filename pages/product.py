from selenium.webdriver.common.by import By
from helpers.general_helpers import Helper
import re

class Products(Helper):
    brand_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Brand"]')
    price_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Price"]')
    color_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Color"]')
    results_number = (By.XPATH, '//span[contains(text(), "items found")]')
    result_items = (By.XPATH, "//div[@id='products']/article/a")

    def filter_option(self, text):
        return (By.XPATH, f"//ul/li/a[.//text()='{text}']")


    def apply_filters(self, brand, price, color):
        self.find_and_click(self.brand_filter_btn)
        self.find_and_click(self.filter_option(brand))
        self.wait_for_filter_applied(brand)

        self.find_and_click(self.price_filter_btn)
        self.find_and_click(self.filter_option(f"${price}.00 and Under"))
        self.wait_for_filter_applied(price)

        self.find_and_click(self.color_filter_btn)
        self.find_and_click(self.filter_option(color))
        self.wait_for_filter_applied(color)


    def get_result_count(self):
        return self.find_elem_ui(self.results_number).text.split(" ")[0]


    def check_brand(self, brand):
        items = self.find_all(self.result_items)
        for item in items:
            item_text = item.text
            if brand in item_text:
                return True
            else:
                self.test_logger.error(f"Brand isn't included in {item_text}")
                return False


    def check_price(self, price):
        items = self.find_all(self.result_items)
        for item in items:
            item_text = item.text
            match = re.search(r"\$([0-9]+\.[0-9]{2})", item_text)
            if match:
                item_price = match.group(1)
                if item_price < price:
                    return True
                else:
                    self.test_logger.error(f"{price} price doesn't match, instead got {item_price}")
                    return False
            else:
                self.test_logger.error(f"Price wasn't found in {item_text}")

