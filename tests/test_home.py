import pdb

import pytest
from selenium import webdriver
import page


class TestHome:

    @pytest.fixture
    def setup_driver(self) -> None:
        self.driver = webdriver.Chrome(r"C:\Testing\chromedriver.exe")
        self.driver.get("http://demostore.supersqa.com/")
        yield
        self.driver.close()

    def test_title(self, setup_driver):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()

    def test_search_hoodie(self, setup_driver):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.enter_search_field("Hoodie")
        assert main_page.is_title_matches(r"Search Results for “Hoodie” – DemoStore")
        assert main_page.read_search_result("Hoodie")
        main_page.check_for_product("Hoodie")


if __name__ == "__main__":
    pytest.main()
