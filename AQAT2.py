from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
url = "https://www.avito.ru/favorites"


def test_add_item_to_favorites(item_url):
    driver.get(item_url)
    add_to_favorites_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()
    driver.get(url)
    favorites_list = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )
    try:
        assert favorites_list.is_displayed()
    except AssertionError:
        print("Товар не добавлен в избранное")



try:
    test_favorites_page_title()
    xpath = '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[2]'
    url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    test_add_item_to_favorites(url)

finally:
    driver.quit()

    #Спасибо за потраченное время)