from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json, os


class Helper:

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def go_to_page(self, url):
        self.driver.get(url)
        self.test_logger.info(f"{url} is opened.")

    def find_elem_ui(self, loc, sec=60):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located(loc)
            )
            return elem
        except Exception as e:
            self.test_logger.error("Element is not vissible.")
            self.test_logger.error(e)

    def find_elem_dom(self, loc, sec=60):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc)
        )
        return elem

    def find_and_click(self, loc, sec=60):
        elem = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))
        elem.click()

    def find_and_send_keys(self, loc, inp_text, sec=60):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)

    def wait_for_filter_applied(self, label_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'//ul[@id="searchSelectedFilters"]//*[contains(text(), "{label_text}")]',
                )
            )
        )

    def load_json_data(self, relative_path):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        file_path = os.path.join(project_root, relative_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found in {file_path}")

        with open(file_path, "r") as f:
            return json.load(f)
