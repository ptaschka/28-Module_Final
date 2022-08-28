#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://promotion.aliexpress.ru/wow/gcp/aer/channel/aer/tmall_localization/7pcZWCh8tW?wh_weex=true&_immersiveMode=true&wx_navbar_hidden=true&wx_navbar_transparent=true&ignoreNavigationBar=true&wx_statusbar_hidden=true'

        super().__init__(web_driver, url)

    # My wishlist
    my_wishlist = WebElement(xpath='//div[@class="nav-wishlist"]')

    # Main search field
    search = WebElement(id='search-key')

    # Search button
    search_run_button = WebElement(xpath='//input[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//div[@class="product-snippet_ProductSnippet__name__152uer"]')

    # Button to sort products by price
    sort_products_by_price = WebElement(xpath='//button[contains(text(), "Цена")]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-spm-anchor-id="a2g2w.productlist.0.i71.67d24c53fWSSzq"]')

    # Check button "Category"
    category_button = WebElement(xpath='//div[contains(text(), "Категории")]')

    # Check sub "Category"
    subsection_button = WebElement(xpath='//div[@class="computerCategory categoryTitle"]')

    # Check link subcategory "Category"
    link_subcategory = WebElement(xpath='//a[contains(text(), "Ноутбуки Apple")]')

    # Check header-category
    header_category = WebElement(xpath='//a[contains(text(), "Дом и сад")]')

    # Verification of the link by the picture of the company's brand - "grohe"
    image_of_brand = WebElement(xpath='//a[@data-spm-anchor-id="a2g0o.tm800008754.gmod-aer_brandbar.undefined"]//img')

    # Check round picture under header-category and check raiting filter
    right_arrow = WebElement(xpath='//div[@style="position: relative;"]//button')
    round_picture = WebElement(xpath='//img[@title="Смарт-часы и браслеты"]')

    # Raiting filter
    check_box_rating = WebElement(xpath='//div[@exp_type="top_related"]')

    # Stars of the products in search results
    raiting_stars = ManyWebElements(xpath='//div[@class="product-snippet_ProductSnippet__score__152uer"]')

    # Check sub "Category"
    subsection_button_1 = WebElement(xpath='//div[@class="phonesCategory categoryTitle"]')
    subsection_button_2 = WebElement(xpath='//div[@class="computerCategory categoryTitle"]')
    subsection_button_3 = WebElement(xpath='//div[@class="electronicsCategory categoryTitle"]')
    subsection_button_4 = WebElement(xpath='//div[@class="homeImprovementCategory categoryTitle"]')
    subsection_button_5 = WebElement(xpath='//div[@class="womenCategory categoryTitle"]')
    subsection_button_6 = WebElement(xpath='//div[@class="menCategory categoryTitle"]')
    subsection_button_7 = WebElement(xpath='//div[@class="toysCategory categoryTitle"]')
    subsection_button_8 = WebElement(xpath='//div[@class="jewelryCategory categoryTitle"]')
    subsection_button_9 = WebElement(xpath='//div[@class="shoesCategory categoryTitle"]')
    subsection_button_10 = WebElement(xpath='//div[@class="gardenCategory categoryTitle"]')
    subsection_button_11 = WebElement(xpath='//div[@class="autoPartsCategory categoryTitle"]')
    subsection_button_12 = WebElement(xpath='//div[@class="beautyCategory categoryTitle"]')
    subsection_button_13 = WebElement(xpath='//div[@class="sportsCategory categoryTitle"]')













