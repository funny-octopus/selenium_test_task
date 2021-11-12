import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page

class YandexTestCase(unittest.TestCase):
    ''' Тестирование Yandex '''

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.get('https://yandex.ru')

    def test_search(self):
        ''' Тестирование поиска '''

        search_page = page.SearchPage(self.driver)
        # проверяем наличие поля поиска
        self.assertTrue(search_page.check_search_field())
        # вводим в поле поиска 'Тензор'
        search_page.search_text_el.set_value('Тензор')
        # проверяем отображение таблицы с подсказками
        self.assertTrue(search_page.check_suggest())
        # нажимаем ENTER
        search_page.search_text_el.set_value(Keys.ENTER)
        # проверяем наличие таблицы результатов
        self.assertTrue(search_page.check_search_result_area())
        # проверяем что в первых 5 результатах есть ссылка на tensor.ru
        self.assertIn('https://tensor.ru/', search_page.get_result_links()[:5])

    def test_images(self):
        ''' Тестирование картинок '''

        search_page = page.SearchPage(self.driver)
        # кликаем на ссылку "Картинки"
        search_page.link_images_el.get_element().click()
        #self.wait.until(EC.new_window_is_opened(self.driver.window_handles))
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        images_page = page.ImagesPage(self.driver)
        # проверяем что перешли на url https://yandex.ru/images/
        self.assertEqual('https://yandex.ru/images/',
                self.driver.current_url.split('?')[0])
        categories = images_page.links_categories_el.get_elements()
        category_text = categories[0].text
        category_link = categories[0].\
                find_element_by_tag_name('a').get_attribute('href')
        # открываем первую категорию
        categories[0].click()
        # проверяем что открылась первая категория
        self.assertEqual(category_link, self.driver.current_url)
        # проверяем, что в поиске нужный текст
        self.assertEqual(category_text,
                images_page.search_text_el.get_value())
        images = images_page.search_result_links_el.get_elements()
        self.wait.until(EC.element_to_be_clickable(
            images_page.search_result_links_el.locator))
        # открываем первую картинку
        images[0].click()
        # проверяем что появилось окно с изображением
        self.assertTrue(images_page.check_media_viewer())
        full_first_image_url = self.driver.current_url
        first_image_url = images_page\
                               .media_viewer_img_el\
                               .get_element().get_attribute('src')
        # нажимаем кнопку вперед
        images_page.media_viewer_next_el.get_element().click()
        self.wait.until(EC.url_changes(full_first_image_url))
        full_second_image_url = self.driver.current_url
        second_image_url = images_page\
                               .media_viewer_img_el\
                               .get_element().get_attribute('src')
        # проверяем что картинка меняется
        self.assertNotEqual(first_image_url, second_image_url)
        # нажимаем кнопку назад
        images_page.media_viewer_prev_el.get_element().click()
        self.wait.until(EC.url_changes(full_second_image_url))
        first_image_url_again = images_page\
                               .media_viewer_img_el\
                               .get_element().get_attribute('src')
        # проверяем, что изображение то же что и изначально
        self.assertEqual(first_image_url, first_image_url_again)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
