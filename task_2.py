# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

browser = webdriver.Chrome()
fix_site = "https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/"
fix_title = "Вход в личный кабинет"

try:
    browser.get(fix_site)
    print("Проверить адрес сайта и заголовок страницы")
    assert browser.current_url == fix_site, "Неверный адрес сайта"
    assert browser.title == fix_title, "Неверный заголовок страницы"

    print("Авторизоваться на сайте")
    sleep(3)  # ждём, когда страница стабилизируется
    # login_input = browser.find_element(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__login']")
    # Не могу понять, почему элемент не находится по атрибуту
    login_input = browser.find_element(By.CSS_SELECTOR, "input[name='Login']")
    login_input.send_keys("lisa_alisa")
    login_input.send_keys(Keys.ENTER)
    sleep(3)  # ждём, когда страница стабилизируется
    # password_input = browser.find_element(By.CSS_SELECTOR, "[data-qa='auth-AdaptiveLoginForm__password']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='Password']")
    action_chains = ActionChains(browser)
    action_chains.move_to_element(password_input).click().send_keys("qazwsx123").perform()
    password_input.send_keys(Keys.ENTER)
    sleep(5)  # ждём полной загрузки страницы
    assert browser.current_url == "https://fix-online.sbis.ru/", "Не загрузился сайт"

    print("Перейти в реестр Контакты")
    contacts_page = "https://fix-online.sbis.ru/page/people"
    title_contacts = "Контакты"
    browser.get(contacts_page)
    sleep(4)  # ждём полной загрузки страницы
    assert browser.current_url == contacts_page, "Неверный адрес страницы"
    assert browser.title == title_contacts, "Неверный заголовок страницы"

    print("Отправить сообщение самому себе")
    search_field = browser.find_element(By.CSS_SELECTOR, ".controls-Field.controls-InputBase__nativeField_hideCustomPlaceholder")
    search_field.send_keys("лисичкина алиса")
    search_field.send_keys(Keys.ENTER)
    sleep(2)  # ждём стабилизации страницы
    plus_btn = browser.find_element(By.CSS_SELECTOR, ".controls-Button__icon.icon-RoundPlus")
    plus_btn.click()
    sleep(5)  # ждём загрузки окна отправки сообщения
    msg_field = browser.find_element(By.CSS_SELECTOR, ".textEditor_slate_Field.textEditor_slate_Container")
    msg_field.send_keys("Ура! Получилось!")
    sleep(3)  # ждём стабилизации страницы
    send_msg_btn = browser.find_element(By.CSS_SELECTOR, ".controls-Button__icon.icon-BtArrow")
    send_msg_btn.click()
    sleep(3)  # ждём отправки сообщения

    print("Убедиться, что сообщение появилось в реестре")
    msg_text = "Ура! Получилось!"
    find_msg = browser.find_element(By.XPATH, f"//div[contains(p, '{msg_text}')]")
    assert find_msg.is_displayed(), "Сообщение не найдено"

    print("Удалить это сообщение и убедиться, что удалили")

    find_msg.click()
    sleep(5)  # ждём загрузки окна сообщения
    del_msg_icon = browser.find_element(By.CSS_SELECTOR, ".icon-Erase")
    del_msg_icon.click()
    sleep(5)  # ждём удаления и стабилизации страницы
    find_msg = browser.find_elements(By.XPATH, f"//*[contains(text(), '{msg_text}')]")
    assert len(find_msg) == 0, "Сообщение не удалилось"

finally:
    browser.quit()
