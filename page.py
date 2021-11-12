from selenium.common.exceptions import NoSuchElementException
from element import SearchTextPageElement, BasePageElement
from locators import SearchPageLocators, ImagesPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_text_el = SearchTextPageElement(
                SearchPageLocators.SEARCH_FIELD,
                self.driver
                )
        self.suggest_el = BasePageElement(
                SearchPageLocators.SUGGEST_FIELD,
                self.driver
                )
        self.result_area_el = BasePageElement(
                SearchPageLocators.SEARCH_RESULT_AREA,
                self.driver
                )
        self.search_result_link_el = BasePageElement(
                SearchPageLocators.SEARCH_RESULT_LINKS,
                self.driver
                )
        self.link_images_el = BasePageElement(
                SearchPageLocators.IMAGES_LINK,
                self.driver
                )

    def check_search_field(self) -> bool:
        search_field = self.search_text_el.get_element()
        return search_field.is_displayed()

    def check_suggest(self) -> bool:
        suggest_field = self.suggest_el.get_element()
        return suggest_field.is_displayed()

    def check_search_result_area(self) -> bool:
        result_area = self.result_area_el.get_element()
        return result_area.is_displayed()

    def get_result_links(self) -> list:
        search_result_links = self.search_result_link_el.get_elements()
        return [el.get_attribute('href') for el in search_result_links]


class ImagesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.links_categories_el = BasePageElement(
                ImagesPageLocators.CATEGORIES_LINKS,
                self.driver
                )
        self.search_text_el = SearchTextPageElement(
                ImagesPageLocators.SEARCH_FIELD,
                self.driver
                )
        self.search_result_links_el = BasePageElement(
                ImagesPageLocators.SEARCH_RESULT_LINKS,
                self.driver
                )
        self.media_viewer_el = BasePageElement(
                ImagesPageLocators.MEDIA_VIEWER,
                self.driver
                )
        self.media_viewer_next_el = BasePageElement(
                ImagesPageLocators.MEDIA_VIEWER_NEXT,
                self.driver
                )
        self.media_viewer_prev_el = BasePageElement(
                ImagesPageLocators.MEDIA_VIEWER_PREV,
                self.driver
                )
        self.media_viewer_img_el = BasePageElement(
                ImagesPageLocators.MEDIA_VIEWER_IMG,
                self.driver
                )

    def check_media_viewer(self) -> bool:
        media_viewer = self.media_viewer_el.get_element()
        return media_viewer.is_displayed()

