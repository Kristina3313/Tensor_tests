from pages.base_page import BasePage
from locators import sbis_locators
import allure


class SbisPage(BasePage):
    @allure.step('Клик по кнопке "Контакты"')
    def click_by_contacts_botton(self):
        self.find_and_click_element(sbis_locators.CONTACTS_BOTTON)

    @allure.step("Клик на кнопку 'Скачать локальные версии' в футере")
    def click_by_download_button(self):
        self.find_and_click_element(sbis_locators.DOWNLOAD_BUTTON)

    @allure.step("Скролл до элемента 'Скачать локальные версии' в футере")
    def scroll_to_download_in_futter(self):
        self.scroll_into_view(sbis_locators.DOWNLOAD_BUTTON)
