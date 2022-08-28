from pages.base import WebPage
from pages.elements import WebElement
from config import url_tmall_login


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url_tmall_login
        super().__init__(web_driver, url)

    email = WebElement(id='email')

    password = WebElement(id='password')

    btn = WebElement(xpath='//button[@type="submit"]')

    invalid_data_msg = WebElement(xpath='//div[@class="ali-kit_Input__wrapper__cjj0j4 wrapper_m"]/span')

    banner = WebElement(xpath='//div[@class="baxia-dialog-close"]')


