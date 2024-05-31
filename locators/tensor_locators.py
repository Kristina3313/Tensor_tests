from selenium.webdriver.common.by import By

# Заголовок 'Сила в людях'
BLOCK_SILA = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
# Кнопка "Подробнее" в блоке 'Сила в людях'
BUTTON_ABOUT = (By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']//p[@class='tensor_ru-Index__card-text']//a[@class='tensor_ru-link tensor_ru-Index__link'][contains(text(),'Подробнее')]")
