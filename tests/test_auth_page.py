import pytest
from pages.auth_page import AuthPage
from config import e_mail, passw, url_tmall, generate_string, russian_chars, chinese_chars, special_chars


# @pytest.mark.xfail(reason="Error because captcha")
# def test_authorisation_with_valid_data(web_browser):
#     """ Check  authorisation with valid data."""
#     page = AuthPage(web_browser)
#     page.email.send_keys(e_mail)
#     page.password.send_keys(passw)
#     page.btn.click()
#     page.wait_page_loaded()
#     assert page.get_current_url() == url_tmall

# @pytest.mark.parametrize("invalid_email",
#                          ['ptaschkaa@mail.com'
#                              , 'p@mail.ru'
#                              , 'ptaschkaa@gmail.ru'
#                              , 'ptaschkaa@mailru'
#                              , 'ptaschkaamail.ru'
#                              , '123@mail.ru'
#                              , '123mail.ru'
#                              , '0'
#                              , generate_string(255)
#                              , generate_string(1001)
#                              , russian_chars()
#                              , russian_chars().upper()
#                              , chinese_chars()
#                              , special_chars()
#                           ], ids=["email с неверным доменом"
#                                   , "несуществующий email"
#                                   , "email с неверной почтовой службой"
#                                   , "email без точки"
#                                   , "email без собаки"
#                                   , "несуществующий email из цифр"
#                                   , "несуществующий email из цифр без собаки"
#                                   , "email со строкой 255 символов"
#                                   , "email со строкой из 1001 символа"
#                                   , "email из русских букв"
#                                   , "email из русских прописных букв"
#                                   , "email из китайских букв"
#                                   , "email из спецсимволов"
#                                   , "просто ноль"
#                                   ])
# def test_authorisation_with_invalid_email(web_browser, invalid_email):
#     """ Parameterized test authorisation with invalid email and valid password."""
#     page = AuthPage(web_browser)
#     page.email.send_keys(invalid_email)
#     page.password.send_keys(passw)
#     page.btn.click()
#     page.wait_page_loaded()
#     page.banner.click()
#     page.wait_page_loaded()
#     assert page.invalid_data_msg.is_presented()
#
# @pytest.mark.parametrize("invalid_passw",
#                          ['зопрjghb854+/'
#                              , '0'
#                              # , generate_string(255)
#                              # , generate_string(1001)
#                              # , russian_chars()
#                              # , russian_chars().upper()
#                              # , chinese_chars()
#                              # , special_chars()
#                           ], ids=["несуществующий пароль"
#                                   , "просто ноль"
#                                   # , "пароль со строкой 255 символов"
#                                   # , "пароль со строкой из 1001 символа"
#                                   # , "пароль из русских букв"
#                                   # , "пароль из русских прописных букв"
#                                   # , "пароль из китайских букв"
#                                   # , "пароль из спецсимволов"
#                                   ])
# def test_authorisation_with_invalid_passw(web_browser, invalid_passw):
#     """ Parameterized test authorisation with valid email and invalid password."""
#     page = AuthPage(web_browser)
#     page.email.send_keys(e_mail)
#     page.password.send_keys(invalid_passw)
#     page.btn.click()
#     page.wait_page_loaded()
#     page.banner.click()
#     page.wait_page_loaded()
#     assert page.invalid_data_msg.is_presented()
#
# def test_authorisation_with_empty_e_mail(web_browser):
#     """ Test authorisation with null email and valid password"""
#     page = AuthPage(web_browser)
#     page.email.send_keys("")
#     page.password.send_keys(passw)
#     assert page.btn.is_clickable() == False
#
# def test_authorisation_with_empty_passw(web_browser):
#     """ Test authorisation with valid email and null password"""
#     page = AuthPage(web_browser)
#     page.email.send_keys(e_mail)
#     page.password.send_keys("")
#     assert page.btn.is_clickable() == False




