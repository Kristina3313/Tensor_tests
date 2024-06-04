from locators import tensor_locators
from pages.base_page import BasePage
import allure


class TensorPage(BasePage):

    @allure.step('Получение заголовка из блока "Сила в людях"')
    def get_text_from_sila_block(self):
        return self.find_element(tensor_locators.BLOCK_SILA).text

    @allure.step('Сколл до блока "Сила в людях"')
    def scroll_to_block_sila(self):
        self.scroll_into_view(tensor_locators.BLOCK_SILA)

    @allure.step('Клик на раздел "Подробнее"')
    def click_by_about_button(self):
        self.find_and_click_element(tensor_locators.BUTTON_ABOUT)
