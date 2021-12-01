import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from error_handling import error_handler as error_handler


def parse_sessions(settings, env):
    logging.info(f"Start parse sessions")
    try:
        logging.debug(f"headless={settings['headless']}")
        logging.debug(f"chromedriver_path={settings['chromedriver_path']}")
        if settings['headless']:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(settings['chromedriver_path'], options=chrome_options)
        else:
            browser = webdriver.Chrome(settings['chromedriver_path'])
        logging.debug(f"browser={browser}")

        # Login в GetCourse
        logging.debug("Try login to GetCourse")
        browser.get("https://givin.school/cms/system/login?required=true")
        logging.debug("Find input login")
        input_login = browser.find_element(By.CSS_SELECTOR, "input.form-control.form-field-email")
        input_login.send_keys(env[0])
        logging.debug("Find input password")
        input_password = browser.find_element(By.CSS_SELECTOR, "input.form-control.form-field-password")
        input_password.send_keys(env[1])
        logging.debug("Find button ОК")
        button = browser.find_element(By.CSS_SELECTOR, ".float-row > .btn-success")
        button.click()
        time.sleep(5)

        # Открыть страницу sessions
        logging.debug("Открыть страницу sessions")
        logging.debug("link=https://givin.school/pl/metrika/traffic/visit-list")
        browser.get("https://givin.school/pl/metrika/traffic/visit-list")
        time.sleep(7)

        # Поиск кнопки Добавить условие и выбор в меню Авторизованный
        logging.debug("Поиск кнопки Добавить условие")
        button_show_more = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default.dropdown")
        button_show_more.click()
        logging.debug("Поиск поля ввода")
        search_input = browser.find_element(By.CSS_SELECTOR, "input.search-input")
        search_input.clear()
        search_input.send_keys("Ав")  # Авторизованный
        # search_input.send_keys(Keys.ENTER)  # В этом поле ENTER не срабатывает, нужно кликать на пункт меню
        logging.debug("Поиск пункта меню Авторизованный")
        menu_item = browser.find_element(By.CSS_SELECTOR, '[data-type="is_user"]')
        menu_item.click()
        # time.sleep(5)

        # Поиск кнопки Выбрать даты и заполнение полей дат
        logging.debug("Поиск кнопки Выбрать даты")
        button_select_dates = browser.find_element(By.CSS_SELECTOR, "span#select2-chosen-4.select2-chosen")
        button_select_dates.click()
        logging.debug("Поиск поля ввода и выбор пункта Выбрать даты")
        search_input = browser.find_element(By.CSS_SELECTOR, "input#s2id_autogen4_search.select2-input")
        search_input.clear()
        search_input.send_keys("Выбрать даты")  # Выбрать даты
        search_input.send_keys(Keys.ENTER)
        # time.sleep(5)
        logging.debug("Поиск поля ввода даты С и ввод даты")
        input_from = browser.find_element(By.CSS_SELECTOR, 'span.from input.form-control')
        input_from.clear()
        input_from.send_keys("01.12.2021")  # с 01.12.2021
        input_from.send_keys(Keys.ENTER)
        logging.debug("Поиск поля ввода даты ПО и ввод даты")
        input_to = browser.find_element(By.CSS_SELECTOR, 'span.to input.form-control')
        input_to.clear()
        input_to.send_keys("01.12.2021")  # по 01.12.2021
        input_to.send_keys(Keys.ENTER)
        time.sleep(5)

        # закрываем браузер после всех манипуляций
        logging.debug("Закрываем браузер после всех манипуляций")
        browser.quit()
    except Exception as e:  # noqa: E722
        error_handler("Ошибка парсинга страницы", do_exit=True)
    finally:
        # закрываем браузер даже в случае ошибки
        browser.quit()
    logging.info(f"End parse sessions")
