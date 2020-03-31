from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_css_selector("#book").click()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)#answer
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_xpath("//button[text()=\"Submit\"]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.close()
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла