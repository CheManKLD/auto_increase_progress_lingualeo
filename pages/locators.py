from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'p.ll-leokit__site-menu__auth-btn')
    SWITCH_TO_LOGIN_BUTTON = (By.CSS_SELECTOR, '.ll-ModalAuthAlt__switch')
    EMAIL_FORM = (By.CSS_SELECTOR, '#app .ll-ModalAuthAlt__front > form > input:nth-child(1)')
    PASSWORD_FORM = (By.CSS_SELECTOR, '#app .ll-ModalAuthAlt__front > form > input:nth-child(2)')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.ll-ModalAuthAlt__submit')


class Course413PageLocators:
    TRY_COURSE_BUTTON = (By.CSS_SELECTOR, '.ll-leokit__learn-course-lessons__module-card-button-green')
    START_COURSE_BUTTON = (By.CSS_SELECTOR, '.ll-leokit__learn-course-lessons__module-card-button')
    CONFIRMATION_BUTTON = (By.CSS_SELECTOR, '.ll-leokit__button__m-color-azul')
    OK_BUTTON = (By.CSS_SELECTOR, '.ll-leokit__button')
    RIGHT_ANSWER_1_CHECKBOX = (By.XPATH, '//*[contains(text(), "чтобы сказать о нахождении предмета в каком-то месте")]')
    RIGHT_ANSWER_2_CHECKBOX = (By.XPATH, '//*[contains(text(), "когда речь идет об одном лице или предмете")]')
    RIGHT_ANSWER_3_CHECKBOX = (By.XPATH, '//*[contains(text(), "когда речь идет о нескольких лицах или предметах")]')
