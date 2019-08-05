from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS()
my_url = 'http://avi.im/stuff/js-or-no-js.html'
priberam = 'https://dicionario.priberam.org/'
driver.get(priberam)
driver.maximize_window()

elem = driver.find_element_by_name('ctl00$wordMeaningContentPlaceHolder$wordMeaningControl$SearchWordTextBox')
elem.clear()
elem.send_keys('boas')
elem = driver.find_element_by_id('searchButton')
elem.click()


# wait = WebDriverWait(driver, 10)
# # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pb-words-list")))
# wait.until(EC.text_to_be_present_in_element((By.ID, "ContentPlaceHolder1_proximas_proximasContent")))

driver.save_screenshot('screenshot.png') # save a screenshot to disk
html = driver.page_source
print(html)

# p_element = driver.find_element_by_id(id_='ContentPlaceHolder1_vizinhos_vizinhosContainer') #
# p_element = driver.find_element_by_id(id_='ContentPlaceHolder1_proximas_proximasContent') # fds
# p_element = driver.find_element_by_id(id_='traduzir_palavra') # works
# print(p_element.text)

# # HTML from `<html>`
# html = driver.execute_script("return document.documentElement.outerHTML;")
# # HTML from `<body>`
# html = driver.execute_script("return document.body.outerHTML;")
# print(html)

driver.quit()