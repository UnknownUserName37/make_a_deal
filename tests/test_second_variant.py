from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# Second way


def test_eto_pizda_test(setup):
    driver = setup
    general_window, all_themes = driver.current_window_handle, driver.find_elements(By.XPATH, "//div[@class = 'title']")
    themes_list = [themes_list for themes_list in all_themes]

    for one_theme in range(len(themes_list)):
        ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(themes_list[one_theme]).perform()
        driver.switch_to.window(driver.window_handles[1])
        text_for_assert = driver.find_element(By.XPATH, "//h1/i").text
        driver.close()
        driver.switch_to.window(general_window)

        assert text_for_assert == themes_list[one_theme].text
