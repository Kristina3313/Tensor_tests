import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на основную страницу')
    def go_to_site(self):
        self.driver.get('https://sbis.ru/')

    def find_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f'Element not found in {locator}')

    def switch_to_new_tab(self, main_window_handle, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda driver: len(self.driver.window_handles) > 1)
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url(self, expected_url, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url), f'URL did not change to {expected_url}')
