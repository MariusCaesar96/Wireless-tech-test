
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

def main():
    json_packages = []
    driver.get('https://wltest.dns-systems.net/')
    packages = driver.find_elements(By.CSS_SELECTOR, '.package')

    for package in packages:
        # grab option title, description, price, discount
        packages_dict = {
            'option_title': package.find_element(By.TAG_NAME, 'h3').text,
            'description': package.find_element(By.CSS_SELECTOR, '.package-name').text,
            'price': package.find_element(By.CSS_SELECTOR, '.price-big').text.replace('£', ''),
            'discount': package.find_element(By.XPATH , '//p[@style="color: red"]').text.replace('£', '')
        }
        # push dict to all_packages list
        json_packages.append(packages_dict)

    # order all packages by highest price first
    json_packages.reverse()
    
    # Convert list to json
    json_str = json.dumps(json_packages, indent=4)

    # print final json to console
    print(json_str)

    driver.close()



if __name__ == '__main__':
    main()
