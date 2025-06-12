from selenium.webdriver.common.by import By
from helpers.general_helpers import Helper
from selenium.webdriver.common.keys import Keys

class Home(Helper): 
    search_input = (By.ID, "searchAll")
    
    def search_product(self, search_data):
        self.find_and_send_keys(self.search_input, search_data + Keys.ENTER)

    
