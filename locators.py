from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    SEARCH_FIELD = (By.ID, 'text')
    SUGGEST_FIELD = (By.CSS_SELECTOR, '.mini-suggest__item')
    SEARCH_RESULT_AREA = (By.CSS_SELECTOR, '.main__content')
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, 'ul#search-result li h2 a')
    IMAGES_LINK = (By.LINK_TEXT, 'Картинки')


class ImagesPageLocators(object):
    CATEGORIES_LINKS = (By.CSS_SELECTOR, '.PopularRequestList-Item')
    SEARCH_FIELD = (By.NAME, 'text')
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, '.serp-item')
    MEDIA_VIEWER = (By.CSS_SELECTOR, '.MediaViewer')
    MEDIA_VIEWER_NEXT = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext')
    MEDIA_VIEWER_PREV = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev')
    MEDIA_VIEWER_IMG = (By.CSS_SELECTOR, '.MMImage-Origin')

