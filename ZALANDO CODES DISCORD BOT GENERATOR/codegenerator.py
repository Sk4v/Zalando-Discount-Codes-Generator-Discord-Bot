from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def code(PATH,link_newsletter,t):
    # PATH = Chrome Driver Installation Path
    # t = time, the program may not work with too low times

    options = Options()
    options.headless=False #set True to use Chrome in headless mode...maybe it doesn't work very well.
    driver = webdriver.Chrome(options=options,executable_path=PATH)
    link_email='https://generator.email/'

    driver.get(link_email)
    email=driver.find_element_by_xpath('//*[@id="email_ch_text"]').text
    print(email)

    #open new chrome tab
    driver.execute_script("window.open('about:blank','tab2');")
    driver._switch_to.window('tab2')
    driver.get(link_newsletter)

    sleep(t)
    while True:
        try:
            print('cookie')
            driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
            break
        except:
            pass

    while True:
        try:
            print('send email')
            driver.find_element_by_xpath('//*[@id="email-input"]').send_keys(email)
            break
        except:
            pass

    sleep(t)
    attempspref=0
    while True:
        try:
            print('finding newsletter preferences')
            woman_fashion = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div/div[1]/div/label')
            woman_fashion.click()
            break
        except:
            attempspref+=1
            if attempspref == 5:
                print('ERROR I could not find the newsletter preferences button')
                break
            pass

    sleep(t)

    attemps=0
    while True:
        try:
            print('finding subscribe button')
            subscribe_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[5]/button')
            subscribe_button.click()
            break
        except:
            sleep(t)
            attemps+=1
            if attemps==5:
                print('ERROR I have not found the button to subscribe')

    #return to the first chrome tab
    driver.switch_to.window(driver.window_handles[0])

    link='https://generator.email/'+email
    driver.quit()
    return link

