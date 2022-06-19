import time

from .base_page import BasePage
from .locators import Course413PageLocators


class Course413Page(BasePage):
    ANSWERS_LOCATORS = [
        Course413PageLocators.RIGHT_ANSWER_1_CHECKBOX,
        Course413PageLocators.RIGHT_ANSWER_2_CHECKBOX,
        Course413PageLocators.RIGHT_ANSWER_3_CHECKBOX,
    ]

    def complete_course(self):
        time.sleep(1)
        element = self.browser.find_element(*Course413PageLocators.START_COURSE_BUTTON)
        element.click()

        for _ in range(3):
            time.sleep(1)
            element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
            element.click()

        for i in range(len(self.ANSWERS_LOCATORS)):
            element = self.browser.find_element(*self.ANSWERS_LOCATORS[i])
            element.click()

            for _ in range(2):
                element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
                element.click()

        element = self.browser.find_element(*Course413PageLocators.BACK_TO_START_COURSE_BUTTON)
        element.click()

        time.sleep(1)
        element = self.browser.find_element(*Course413PageLocators.TRY_COURSE_BUTTON)
        element.click()
        element = self.browser.find_element(*Course413PageLocators.OK_BUTTON)
        element.click()
