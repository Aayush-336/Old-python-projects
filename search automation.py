from selenium import webdriver
# import random
import time

# for i in range(2):
driver = webdriver.Chrome()
driver.get('https://www.ssrmovies.site')
searchbox = driver.find_element_by_xpath('//*[@id="s"]')

searchbox.send_keys('Avengers Endgame')

searchbox.submit()

time.sleep(5)
# driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div[2]/div/div[4]/div[1]/div[1]/div/div/a[1]/div').click()
# driver.close()
driver.find_element_by_xpath('//*[@id="content_box"]/article[2]/header/h2/a').click()
time.sleep(3)
# driver= driver.switch_to_default_content()
# driver.back()
# driver.close()
# time.sleep(15)
# comment=driver.find_element_by_xpath('//*[@id="comment"]')
# comment.click()
# comment.send_keys('This is the best movie')
# name=driver.find_element_by_xpath('//*[@id="author"]')
# name.click()
# name.send_keys('fan of endgame')
# email=driver.find_element_by_xpath('//*[@id="email"]')
# email.click()
#
# email.send_keys(f'engamelover{random.randint(0,300)}@gmail.com')
# # driver.refresh()
# driver.find_element_by_xpath('//*[@id="submit"]').click()
# driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
# driver.find_element_by_xpath('//*[@id="button"]').click()
# driver.find_element_by_xpath('//*[@id="subscribe-button"]').click()
# driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]').click()
# driver.find_element_by_link_text('https://www.youtube.com/channel/UCMrW_BDWQ0WCvvgmoRfbIfw/videos').click()
# driver.find_element_by_id('button').click()
# driver.find_element_by_id('text').click()
# searchbox.send_keys("hello")
# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchbutton.click()
