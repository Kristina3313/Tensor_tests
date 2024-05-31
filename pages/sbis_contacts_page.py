from pages.base_page import BasePage
from locators import sbis_conacts_locators
import allure


class SbisContactsPage(BasePage):
    @allure.step('Клик по баннеру "Тензор" и переключение на новую вкладку')
    def click_by_tensor_banner(self):
        self.find_and_click_element(sbis_conacts_locators.LOGO_TENSOR)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)
