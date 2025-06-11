import data.config as config
from Pages.home import Home
from Pages.product import Products

def test_case(test_driver, test_logger):

    # activate Chrome browser
    home_page = Home(test_driver, test_logger)
    home_page.go_to_page(config.URL)

    # enter 6pm wesbite and search
    data = home_page.load_json_data("data/test_data.json")
    home_page.search_product(data.get("search"))

    # navigate to product page and apply filters
    product_page = Products(test_driver, test_logger)
    product_page.apply_filters(data.get("brand"), data.get("price"), data.get("color"))
    
    # log number of results
    results = product_page.find_elem_ui(product_page.results_number).text.split(" ")[0]
    test_logger.info(f"{results} product(s) were found.")
    
    # assert results match search data
    brand, price = product_page.get_brand_and_price()
    assert brand == data.get("brand"), test_logger.error(f"The brand doesn't match, instead got {brand}")
    assert price < int(data.get("price")), test_logger.error(f"The price doesn't match, instead got {price}")
