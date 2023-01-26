from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# First way

def test_eto_pizda_test(setup):
    driver = setup

    general_window = driver.current_window_handle

    ALL_THEMES = driver.find_elements(By.XPATH, "//div[@class = 'title']")
    themes_list = [themes_list for themes_list in ALL_THEMES]

    action = ActionChains(driver)

    for one_theme in range(len(themes_list)):
        text_for_assert = None

        action.key_down(Keys.LEFT_CONTROL).click(themes_list[one_theme]).perform()

        handles = driver.window_handles[1]
        driver.switch_to.window(handles)

        text_for_assert = driver.find_element(By.XPATH, "//h1/i").text

        driver.close()
        driver.switch_to.window(general_window)

        assert text_for_assert == themes_list[one_theme].text
