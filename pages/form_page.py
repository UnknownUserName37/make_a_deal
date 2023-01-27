from locators.locators import Locators
from pages.base_page import BasePage


class FormPage(BasePage):

    def all_elements_what_we_are_need(self):
        thems_list = self.elements_are_visible(Locators.LIST_OF_THEMES).text
        result_list = [i.text for i in thems_list]
        print(result_list)
        return result_list
