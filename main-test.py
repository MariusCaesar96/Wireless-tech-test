import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

class TestTitle(unittest.TestCase):
    def test_title(self):
        driver.get('https://wltest.dns-systems.net/')
        packages = driver.find_elements(By.CSS_SELECTOR, '.package')
        self.assertEqual(len(packages), 6, 'Should be 6')

if __name__ == '__main__':
    unittest.main()