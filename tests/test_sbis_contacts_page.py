import allure
from conftest import driver
from pages.sbis_page import SbisPage
from pages.sbis_contacts_page import SbisContactsPage


@allure.story('Тест на странице "Контакты/Sbis"')
class TestSbisContactsPage:

    # Сценарий №2
    @allure.title('Тест определения региона и заголовка в списке партнёров')
    def test_get_region_and_cty_from_contacts_list(self, driver):
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        sbis_page.click_by_contacts_botton()
        sbis_contacts_page = SbisContactsPage(driver)
        region = sbis_contacts_page.get_region()
        city = sbis_contacts_page.get_city_from_contacts_list()
        assert "Республика Башкортостан" in region and "Уфа" in city

    # Сценарий №2
    @allure.title('Тест смены региона')
    def test_change_region(self, driver):
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        sbis_page.click_by_contacts_botton()
        sbis_contacts_page = SbisContactsPage(driver)
        sbis_contacts_page.click_by_current_region()
        sbis_contacts_page.choose_krasnodarsky_kray_in_region_list()
        sbis_contacts_page.wait_change_region_in_url()
        region = sbis_contacts_page.get_region()
        city = sbis_contacts_page.get_city_from_contacts_list()
        assert "Краснодарский край" in region and "Краснодар" in city
