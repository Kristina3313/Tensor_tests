from locators import tensor_about_locators
from pages.base_page import BasePage
import allure


class TensorAboutPage(BasePage):

    @allure.step("Скролл до первой картинки в блоке 'Работаем'")
    def scroll_to_work_block(self):
        self.scroll_into_view(tensor_about_locators.FIRST_PICTURE)

    @allure.step('Получение размеров первого изображения в блоке "Работаем"')
    def get_size_from_first_img(self):
        size = self.find_element(tensor_about_locators.FIRST_PICTURE).size
        return size

    @allure.step('Получение размеров второго изображения в блоке "Работаем"')
    def get_size_from_second_img(self):
        size = self.find_element(tensor_about_locators.SECOND_PICTURE).size
        return size

    @allure.step('Получение размеров третьего изображения в блоке "Работаем"')
    def get_size_from_third_img(self):
        size = self.find_element(tensor_about_locators.THIRD_PICTURE).size
        return size

    @allure.step('Получение размеров четвёртого изображения в блоке "Работаем"')
    def get_size_from_fourth_img(self):
        size = self.find_element(tensor_about_locators.FOURTH_PICTURE).size
        return size
