from selenium.webdriver.common.by import By

# Кнопка "Контакты" в хэдере
CONTACTS_BOTTON = (By.XPATH, "//a[@class='sbisru-Header__menu-link sbisru-Header__menu-link--hover'][contains(text(),'Контакты')]")
# Кнопка "Скачать локальные версии" в футере
DOWNLOAD_BUTTON = (By.XPATH, "//a[contains(text(),'Скачать локальные версии')]")
