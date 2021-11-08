from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def fcode(PATH,link):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.get(link)
    code=driver.find_element_by_xpath('//*[@id="email-table"]/div[2]/div[4]/div[3]/table[2]/tbody/tr/td/table/tbody/tr/td/table[7]/tbody/tr/td/table[2]/tbody/tr/td/table[4]/tbody/tr/td[1]').text
    print(code)
    driver.quit()
    return code