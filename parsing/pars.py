import time
import undetected_chromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from reCaptha import *

i = 2

def ma():
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')

    driver = undetected_chromedriver.Chrome(executable_path="chromedriver", options=options)
    driver.maximize_window()
    driver.get(url=url)

    try:
        time.sleep(15)

        driver.find_element(By.ID, "LanguageId").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[text()='Russian']").click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        #               Ввод Email
        driver.find_element(By.ID, "EmailId").send_keys("Пишем свой email")


        time.sleep(1)

        #               Ввод Password
        driver.find_element(By.ID, "Password").send_keys("Пароль")
        time.sleep(1)

        #               Прохождение капчи
        driver.execute_script('document.getElementById("g-recaptcha-response").style.display = null;')
        res = cap()

        while True:
            captha_token = check_cap(res)
            if captha_token != "CAPCHA_NOT_READY":
                driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]').send_keys(captha_token)
                break
            else:
                print(captha_token)
                time.sleep(2)

        #               Кнопка войти
        driver.find_element(By.ID, "btnSubmit").click()
        time.sleep(15)

        #               Вход на регистрацию визы
        driver.find_element(By.XPATH, xPATH).click()
        time.sleep(4)

        #               Выбор города и вид визы
        located(driver, i)

        #               Ввод данных для регестраци визы
        driver.find_element(By.ID, "PassportNumber").send_keys("12345678")
        time.sleep(1)

        driver.find_element(By.ID, "DateOfBirth").send_keys("12011999")
        time.sleep(1)

        driver.find_element(By.ID, "PassportExpiryDate").send_keys("02032025")
        time.sleep(1)

        driver.find_element(By.ID, "NationalityId").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[text()='BELARUS']").click()
        time.sleep(1)

        firstName = driver.find_element(By.ID, "FirstName")
        firstName.clear()
        firstName.send_keys("Ivanushka")
        time.sleep(1)

        lastName = driver.find_element(By.ID, "LastName")
        lastName.clear()
        lastName.send_keys("Ivanov")
        time.sleep(1)

        driver.find_element(By.ID, "GenderId").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[text()='Мужской']").click()
        time.sleep(1)

        driver.find_element(By.ID, "Mobile").clear()
        driver.find_element(By.ID, "Mobile").send_keys("323367")
        time.sleep(1)

        driver.find_element(By.ID, "validateEmailId").clear()
        driver.find_element(By.ID, "validateEmailId").send_keys("IvanNyshka@gmail.com")
        time.sleep(1)

        driver.find_element(By.ID, "submitbuttonId").click()
        time.sleep(3)

        pyautogui.press('enter')
        time.sleep(5)

        driver.find_element(By.ID, "sndOTP").click()
        time.sleep(204.9)


        #                   Функция получения кода из письма
        MailCode()



    except Exception as ex:
        print("ТУТ ГДЕ-ТО ОШИБКА\n",ex)
        # driver.quit()
        ma()


# Функция получения кода из письма
def MailCode():
    url = "https://mail.google.com/"

    driver = undetected_chromedriver.Chrome(executable_path="chromedriver")
    driver.get(url=url)

    time.sleep(10)
    driver.find_element(By.ID, "identifierId").send_keys("say.meow201@gmail.com\n")

    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("vfsGlobal20@78\n")

    time.sleep(180)
    driver.find_element(By.XPATH, '//span=[text="OTP Confirmation Email"]').click()
    time.sleep(39000)


# выбор города
def located(driver, i):
    driver.find_element(By.ID, "LocationId").click()
    time.sleep(2)

    driver.find_element(By.XPATH, f'//*[@id="LocationId"]/option[{i}]').click()
    time.sleep(3)

    driver.find_element(By.ID, f'VisaCategoryId').click()
    time.sleep(2)

    i += 1
    if i == 15:
        i -= 13

    try:
        # Доработать: программа запрашивает какой вид визы нужен
        driver.find_element(By.XPATH, f"//option[text()='D-visa Students']").click()
        time.sleep(5)

        driver.find_element(By.ID, f'btnContinue').click()
        time.sleep(10)

    #     проверить есть ли кнопка продолжить на след странице если нет
        if xpath_exists(driver, "//a[text()='Добавить Клиента']"):
            driver.find_element(By.XPATH, "//a[text()='Добавить Клиента']").click()
            time.sleep(15)
        else:
            located(driver, i)

    except:
        located(driver, i)


# проверка можно ли зарегестрировать визу
def xpath_exists(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        exist = True
    except NoSuchElementException:
        exist = False
    return exist



if __name__ == '__main__':
    ma()
    # MailCode()
