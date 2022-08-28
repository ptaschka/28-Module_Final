Introduction
------------

This project contains tests with usage PageObject
pattern with Selenium and Python (PyTest + Selenium).

Files
-----

[conftest.py] contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py] contains PageObject pattern implementation for Python.

[pages/elements.py] contains helper class to define web elements on web pages.

[pages/auth_page.py] contains elements for authorisation.

[pages/tmall.py] contains elements for check of website elements.

[tests/test_auth_page.py] contains tests of authorisation.
Tests:
1.Check authorisation with valid data
2.Parameterized test authorisation with invalid email and valid password
3.Parameterized test authorisation with valid email and invalid password
4.Test authorisation with empty email and valid password
5.Test authorisation with valid email and empty password
6.Test authorisation with empty email and empty password
[tests/test_smoke_tmall.py] contains several smoke Web UI tests for Tmall (https://promotion.aliexpress.ru/wow/gcp/aer/channel/aer/tmall_localization/7pcZWCh8tW?wh_weex=true&_immersiveMode=true&wx_navbar_hidden=true&wx_navbar_transparent=true&ignoreNavigationBar=true&wx_statusbar_hidden=true)
Tests:
1.Make sure main search works fine
2.Make sure that wrong keyboard layout input works fine
3.Make sure that sort by price works fine
4.Make sure that link of subcategory works fine
5.Make sure that link by the picture of the company's brand works fine
6.Make sure that raiting filter works fine
7.Make sure that subcategory 1-13 works fine
8.Make sure that logo is address aliexpress
9.If you click my wishlist you need to pass autorisation
10.If you click baset you are on page aliexpress
11.Check change currency in goods
12.Negative tests of search
13.Check conversion to card of good

How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```
2) Run tests:

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py
python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_smoke_tmall.py

