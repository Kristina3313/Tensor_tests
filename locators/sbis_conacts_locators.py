from selenium.webdriver.common.by import By

# Кнопка с лого "Тензор"
LOGO_TENSOR = (By.XPATH, "//img[@alt='Разработчик системы СБИС — компания «Тензор»'][1]")
# Получение текущего региона
CURRENT_REGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']")
# Получение заголовка из списка партнёров
CITY_FROM_CONTACTS_LIST = (By.XPATH, "//div[@id='city-id-2']")
#
KRASNODARSKY_KRAY_IN_DIALOG_WINDOW = (By.XPATH, "//span[contains(text(),'23 Краснодарский край')]")
