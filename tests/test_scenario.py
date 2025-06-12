import data.config as config
from pages.home import Home
from pages.product import Products

def test_case(test_driver, test_logger):

    # activate Chrome browser
    home_page = Home(test_driver, test_logger)
    home_page.go_to_page(config.URL)

    # enter 6pm wesbite and search
    data = home_page.load_json_data("data/test_data.json")
    home_page.search_product(data.get("search"))

    product_page = Products(test_driver, test_logger)
    product_page.apply_filters(data.get("brand"), data.get("price"), data.get("color"))
    
    # log number of results
    results = product_page.get_result_count()
    test_logger.info(f"{results} product(s) were found.")
    
    # assert results match search data
    assert product_page.check_brand(data.get("brand"))
    assert product_page.check_price(data.get("price"))