from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a website
a='https://rahulshettyacademy.com/'
driver.get(a)
driver.maximize_window();
b=driver.title;
print(b)
print(driver.current_url)

# Find an element and interact with it
# search_box = driver.find_element_by_name("q")
# search_box.send_keys("pycon")
# search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Close the WebDriver
# driver.quit()
