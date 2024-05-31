import allure
from conftest import driver
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_page import SbisPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_page import TensorPage


@allure.story('Тест на странице "Тензор/about"')
class TestTensorAboutPage:

    @allure.title('Тест редиректа при клике на кнопку "Подробнее"')
    def test_redirect_to_about_page(self, driver):
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        sbis_page.click_by_contacts_botton()
        sbis_contacts_page = SbisContactsPage(driver)
        sbis_contacts_page.click_by_tensor_banner()
        tensor_page = TensorPage(driver)
        tensor_page.scroll_to_block_sila()
        tensor_page.click_by_about_button()
        assert driver.current_url == 'https://tensor.ru/about'

    @allure.title('Проверка размеров фото в блоке "Работаем"')
    def test_img_size_in_work_block(self, driver):
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        sbis_page.click_by_contacts_botton()
        sbis_contacts_page = SbisContactsPage(driver)
        sbis_contacts_page.click_by_tensor_banner()
        tensor_page = TensorPage(driver)
        tensor_page.scroll_to_block_sila()
        tensor_page.click_by_about_button()
        tensor_about_page = TensorAboutPage(driver)
        tensor_about_page.scroll_to_work_block()
        first_img = tensor_about_page.get_size_from_first_img()
        second_img = tensor_about_page.get_size_from_second_img()
        third_img = tensor_about_page.get_size_from_third_img()
        fourth_img = tensor_about_page.get_size_from_fourth_img()
        assert first_img == second_img == third_img == fourth_img
