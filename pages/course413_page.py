import time

from .base_page import BasePage
from .locators import Course413PageLocators


class Course413Page(BasePage):
    def complete_course(self):
        element = self.browser.find_element(*Course413PageLocators.TRY_COURSE_BUTTON)
        element.click()
        element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
        element.click()
        time.sleep(1)
        element = self.browser.find_element(*Course413PageLocators.TRY_COURSE_BUTTON)
        element.click()

        for _ in range(3):
            time.sleep(1)
            element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
            element.click()

        element = self.browser.find_element(*Course413PageLocators.RIGHT_ANSWER_1_CHECKBOX)
        element.click()

        for _ in range(2):
            element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
            element.click()

        element = self.browser.find_element(*Course413PageLocators.RIGHT_ANSWER_2_CHECKBOX)
        element.click()

        for _ in range(2):
            element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
            element.click()

        element = self.browser.find_element(*Course413PageLocators.RIGHT_ANSWER_3_CHECKBOX)
        element.click()

        for _ in range(2):
            element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
            element.click()
