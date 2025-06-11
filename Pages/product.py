from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper

class Products(Helper):
    brand_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Brand"]')
    price_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Price"]')
    color_filter_btn = (By.CSS_SELECTOR, '[data-test-id-facet-head-name="Color"]')
    results_number = (By.XPATH, '//*[contains(text(), "items found")]')
    
    product_brand = (By.XPATH, "//div[@id='products']//dt[text()='Brand Name']/following-sibling::dd[1]/span")
    product_price = (By.XPATH, "//div[@id='products']//dt[text()='Price']/following-sibling::dd[1]//span[contains(text(), '$')]")


    def filter_option(self, text):
        return (By.XPATH, f"//ul/li/a[.//text()='{text}']")

    def get_brand_and_price(self):
        brand = self.find_elem_ui(self.product_brand).text.strip()
        price_text = self.find_elem_ui(self.product_price).text.strip().replace('$', '')
        return brand, float(price_text)

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