from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def facebook_login():
    url = "https://www.facebook.com"
    email = "abc@gmail.com"
    password = "test"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    try:
        driver.find_element_by_id('u_0_h').click()
    except:
        print("No such element found related to accept cookies")
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('u_0_b').click()

facebook_login()

# To press Escape KEY
#driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)