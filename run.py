import time

from selenium.webdriver import DesiredCapabilities

from pages.course413_page import Course413Page


def get_10_percent_of_progress(times=1):
    """
    Функция для получения 10% ежедневного прогресса на Lingualeo
    :param times: количество раз получения 10% ежедневного прогресса
    :return: None
    """

    if (not isinstance(times, int)) or times < 1:
        raise ValueError('введите целое положительное число')

    course_413_page_url = 'https://lingualeo.com/ru/course/413'
    link = course_413_page_url

    # меняем стратегию работы Selenium с normal (ожидание полной загрузки страницы)
    # на eager (когда страница становится интерактивной)
    caps = DesiredCapabilities().CHROME.copy()
    caps["pageLoadStrategy"] = "eager"

    page = Course413Page(link, caps=caps)
    page.open()
    page.login()

    time.sleep(1)

    # выпоняем курс необходимое количество раз
    for _ in range(times):
        page.complete_course()

    page.quit()


if __name__ == '__main__':
    get_10_percent_of_progress(10)
