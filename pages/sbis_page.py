from pages.base_page import BasePage
from locators import sbis_locators
import allure


class SbisPage(BasePage):
    @allure.step('Клик по кнопке "Контакты"')
    def click_by_contacts_botton(self):
        self.find_and_click_element(sbis_locators.CONTACTS_BOTTON)
