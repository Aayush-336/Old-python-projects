# import pywhatkit
from selenium import webdriver
import time
import keyboard

# pywhatkit.sendwhatmsg("+919998188432","Chal be phone muk",18,17)
# pywhatkit.sendwhatmsg_with_selenium("+919898710778","Hello",18,21)
dic = ['+919998188432', '+919824098140', '9426609614']
# for k,i in dic.items():
#     pywhatkit.sendwhatmsg(i,"hello  ..",18,43)
# pywhatkit.search('het')
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/label/input').click()
time.sleep(7)
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

for i in dic:
    search.send_keys(i)
    # time.sleep(15)
    # search.submit()
    keyboard.press("enter")
    # time.sleep(2)
    # driver.find_element_by_class_name('eJ0yJ').click()
    txtbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    txtbox.send_keys('Enter your text here')
    # time.sleep(1)
    btn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')

    btn.click()
    search.clear()
# pos= driver.get_window_position()
# print(pos)
# driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]').click()
# time.sleep(1)
# driver.close()
