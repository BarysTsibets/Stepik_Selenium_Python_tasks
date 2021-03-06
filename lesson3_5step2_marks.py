import pytest
from selenium import webdriver

"""Choosing tests with different marks"""
# pytest -s -v -m smoke Automation\lesson3_5step2_marks.py
# pytest -s -v -m 'not smoke' Automation\lesson3_5step2_marks.py
# pytest -s -v -m 'smoke or regressional' Automation\lesson3_5step2_marks.py
# pytest -s -v -m 'smoke and for_win_10l' Automation\lesson3_5step2_marks.py


link = "http://selenium1py.pythonanywhere.com/"
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=PATH)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    @pytest.mark.for_win_10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


