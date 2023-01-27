from selenium.webdriver.common.by import By


class Locators:
    LIST_OF_THEMES = (By.XPATH, "//div[@class = 'title']")
    TEXT_FOR_ASSERT_INSIDE_HEAD = (By.XPATH, "//h1/i")
