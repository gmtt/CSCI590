from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# config part
USER_NAME = input('username: ')
PASSWD = input('password: ')

driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://piazza.com/")

# login part
driver.find_element_by_id('login_button').click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='login-modal modal fade in']")))
inputField = driver.find_element(by=By.ID, value='email_field')
inputField.send_keys(USER_NAME)
inputField = driver.find_element(by=By.ID, value='password_field')
inputField.send_keys(PASSWD)
inputField.submit()

# traverse group
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'question_group')))
groups = driver.find_elements_by_css_selector("div.question_group")
for group in groups:
    posts = group.find_elements_by_css_selector("li[data-pats='post_group_item']")
    for post in posts:
        print(post.find_element_by_class_name('title_text').text)
        post.click()


