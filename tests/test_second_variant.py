from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


# Second way. Yes?


def test_eto_pizda_test(setup):
    driver = setup
    general_window = driver.current_window_handle
    headers_off_all_articles = driver.find_elements(By.XPATH, "//div[@class = 'title']")

    for header_of_one_article in headers_off_all_articles:
        text_of_one_header = header_of_one_article.text
        ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(header_of_one_article) \
            .key_up(Keys.LEFT_CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.find_element(By.XPATH, "//h1/i").text == text_of_one_header
        driver.close()
        driver.switch_to.window(general_window)
