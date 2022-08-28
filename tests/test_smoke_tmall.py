#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run:
#  1) Install all requirements:
#     pip install -r requirements.txt
#  2) Run tests:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_smoke_tmall.py

import pytest
from pages.tmall import MainPage


# def test_check_main_search(web_browser):
#     """ Make sure main search works fine. """
#     page = MainPage(web_browser)
#
#     page.search = 'чемодан'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'чемодан' or 'кейс' in title.lower(), msg

#
# def test_check_wrong_input_in_search(web_browser):
#     """ Make sure that wrong keyboard layout input works fine. """
#     page = MainPage(web_browser)
#
#     # Try to enter "ноутбук" with English keyboard:
#     page.search = 'yjen,er'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'ноутбук' or '' in title.lower(), msg


# def test_check_sort_by_price(web_browser):
#     """ Make sure that sort by price works fine. """
#     page = MainPage(web_browser)
#
#     page.search = 'планшет'
#     page.search_run_button.click()
#
#     # Scroll to element before click on it to make sure
#     # user will see this element in real browser
#     # page.sort_products_by_price.scroll_to_element()
#     page.wait_page_loaded()
#     page.sort_products_by_price.click()
#     page.wait_page_loaded()
#
#     # Get prices of the products in Search results
#     all_prices = page.products_prices.get_text()
#
#     # Convert all prices from strings to numbers
#     all_prices = [float(p.replace(' ', '')) for p in all_prices]
#
#     print(all_prices)
#     print(sorted(all_prices))
#
#     # Make sure products are sorted by price correctly:
#     assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

# def test_check_link_subcategory(web_browser):
#     """ Make sure that link of subcategory works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button.right_mouse_click()
#     page.link_subcategory.click()
#
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'apple' in title.lower(), msg

# def test_check_link_brand(web_browser):
#     """ Make sure that link by the picture of the company's brand works fine. """
#     page = MainPage(web_browser)
#     page.header_category.click()
#     page.image_of_brand.find()
#     page.image_of_brand.click()
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'grohe' in title.lower(), msg

# def test_check_round_picture(web_browser):
#     """ Make sure that raiting filter works fine. """
#     page = MainPage(web_browser)
#     page.right_arrow.click()
#     page.right_arrow.click()
#     page.right_arrow.click()
#     page.right_arrow.click()
#     page.round_picture.click()
#     page.check_box_rating.click()
#
#     for star in page.raiting_stars.get_text():
#         msg = 'Wrong product in search "{}"'.format(star)
#         assert '4,9' or '5,0' in star.lower(), msg

# def test_check_subcategory_1_3(web_browser):
#     """ Make sure that subcategory 1-3 works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button_1.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_2.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_3.click()
#     assert page.products_titles.count() > 0

# def test_check_subcategory_4_6(web_browser):
#     """ Make sure that subcategory 4-6 works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button_4.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_5.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_6.click()
#     assert page.products_titles.count() > 0
#
# def test_check_subcategory_7_9(web_browser):
#     """ Make sure that subcategory 7-9 works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button_7.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_8.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_9.click()
#     assert page.products_titles.count() > 0

# @pytest.mark.xfail(reason="don't work click on "и")
# def test_check_subcategory_10(web_browser):
#     """ Make sure that subcategory 10 works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button_10.wait_to_be_clickable()
#     page.subsection_button_10.click()
#     page.wait_page_loaded()
#     assert page.products_titles.count() > 0

# def test_check_subcategory_11_14(web_browser):
#     """ Make sure that subcategory 11-14 works fine. """
#     page = MainPage(web_browser)
#     page.category_button.click()
#     page.subsection_button_11.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_12.click()
#     assert page.products_titles.count() > 0
#     page.go_back()
#     page.category_button.click()
#     page.subsection_button_13.click()
#     assert page.products_titles.count() > 0

