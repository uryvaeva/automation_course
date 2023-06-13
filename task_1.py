# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
sbis_site = "https://sbis.ru/"
sbis_title = "СБИС — экосистема для бизнеса: учет, управление и коммуникации"

try:
    browser.get(sbis_site)
    sleep(1)
    print("Проверить адрес сайта и заголовок страницы")
    assert browser.current_url == sbis_site, "Неверный адрес сайта"
    assert browser.title == sbis_title, "Неверный заголовок страницы"

    print("Проверить отображение четырех вкладок")
    tabs = browser.find_elements(By.CSS_SELECTOR, ".sbisru-Header__menu-item")
    assert len(tabs) == 4

    print("Проверить текст, атрибут и видимость вкладки Контакты")
    button_txt = "Контакты"
    # contacts_tab = browser.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm")
    # Не могу понять, почему не находится элемент по CSS-селектору
    contacts_tab = browser.find_element(By.XPATH, "//a[text()='Контакты']")
    assert contacts_tab.is_displayed(), "Вкладка Контакты не отображается на странице"
    assert contacts_tab.text == button_txt, "Неверный текст вкладки Контакты"
    assert contacts_tab.get_attribute("href") == "https://sbis.ru/contacts", "Неверная ссылка у вкладки Контакты"

    print("Перейти в раздел Контакты, проверить адрес и заголовок страницы")
    contacts_tab.click()
    assert "https://sbis.ru/contacts" in browser.current_url
    assert browser.title == "СБИС Контакты — г. Москва"

    print("Найти баннер Тензора, проверить его видимость")
    sleep(1)  # Для стабильности теста
    tensor_banner = browser.find_element(By.CSS_SELECTOR, "[title='tensor.ru']")
    assert tensor_banner.is_displayed(), "Баннер Тензор не отображается"

    print("Перейти на https://tensor.ru/")
    tensor_banner.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://tensor.ru/', 'Неверный адрес страницы'

    print("Проверить, что есть блок новости 'Сила в людях'")
    news_block = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__card-title")
    browser.execute_script("return arguments[0].scrollIntoView(true);", news_block)
    assert news_block.is_displayed(), "Блок новости 'Сила в людях' не отображается"

    print("Перейти в 'Подробнее' и убедиться, что открывается https://tensor.ru/about")
    more = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-link.tensor_ru-Index__link[href='/about']")
    browser.execute_script("arguments[0].scrollIntoView();", more)
    more.click()
    sleep(1)
    assert browser.current_url == "https://tensor.ru/about", "Неправильный адрес сайта"

finally:
    browser.quit()
