import allure
from conftest import driver
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


@allure.story('Тест на главной странице "Тензор"')
class TestTensorPage:
    # Сценарий №1
    @allure.title("Наличие блока 'Сила в людях'")
    def test_check_text_from_block(self, driver):
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        sbis_page.click_by_contacts_botton()
        sbis_contacts_page = SbisContactsPage(driver)
        sbis_contacts_page.click_by_tensor_banner()
        tensor_page = TensorPage(driver)
        tensor_page.scroll_to_block_sila()
        text = tensor_page.get_text_from_sila_block()
        assert "Сила в людях" in text
