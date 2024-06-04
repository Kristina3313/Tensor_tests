from pages.base_page import BasePage
from locators import sbis_conacts_locators
import allure


class SbisContactsPage(BasePage):
    @allure.step('Клик по баннеру "Тензор" и переключение на новую вкладку')
    def click_by_tensor_banner(self):
        self.find_and_click_element(sbis_conacts_locators.LOGO_TENSOR)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)

    @allure.step('Получение текста из блока "Регион"')
    def get_region(self):
        return self.find_element(sbis_conacts_locators.CURRENT_REGION).text

    @allure.step('Получение заголовка города из списка партнёров')
    def get_city_from_contacts_list(self):
        return self.find_element(sbis_conacts_locators.CITY_FROM_CONTACTS_LIST).text

    @allure.step("Клик на блок с названием текущего региона")
    def click_by_current_region(self):
        self.find_and_click_element(sbis_conacts_locators.CURRENT_REGION)

    @allure.step("Клик на регион 'Краснодарский край' в списке регионов")
    def choose_krasnodarsky_kray_in_region_list(self):
        self.find_and_click_element(sbis_conacts_locators.KRASNODARSKY_KRAY_IN_DIALOG_WINDOW)

    @allure.step("Ожидание смены региона в URL")
    def wait_change_region_in_url(self):
        self.wait_for_url("https://sbis.ru/contacts/23-krasnodarskij-kraj?tab=clients")

