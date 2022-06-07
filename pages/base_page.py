import os

from dotenv import load_dotenv
from selenium import webdriver

from .locators import BasePageLocators

load_dotenv()


class BasePage:
    def __init__(self, url, caps=None, timeout=5):
        # применяем дополнительные настройки для вебдрайвера Chrome
        if caps:
            self.browser = webdriver.Chrome(desired_capabilities=caps)
        else:
            self.browser = webdriver.Chrome()
        self.url = url
        self.browser.implicitly_wait(timeout)

    def login(self):
        element = self.browser.find_element(*BasePageLocators.SIGNIN_BUTTON)
        element.click()
        element = self.browser.find_element(*BasePageLocators.SWITCH_TO_LOGIN_BUTTON)
        element.click()

        input1 = self.browser.find_element(*BasePageLocators.EMAIL_FORM)
        input1.send_keys(os.getenv('EMAIL'))  # сюда вставляем ваш email от аккаунта на Lingualeo
        input2 = self.browser.find_element(*BasePageLocators.PASSWORD_FORM)
        input2.send_keys(os.getenv('PASSWORD'))  # сюда вставляем ваш пароль от аккаунта на Lingualeo
        element = self.browser.find_element(*BasePageLocators.LOGIN_SUBMIT_BUTTON)
        element.click()

    def open(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()
