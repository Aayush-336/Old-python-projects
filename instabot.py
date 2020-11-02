from selenium import webdriver
from time import sleep


def get_diff():
    folers = open(char_name + 'followers.txt')
    foling = open(char_name + 'following.txt')
    a = folers.readlines()
    b = foling.readlines()
    a2 = []
    b2 = []
    for i in a:
        i = i.strip('\n')
        a2.append(i)
    for i in b:
        i = i.strip('\n')
        b2.append(i)
    # print(a2)
    # print(b2)
    print("Not following back")
    for i in b2:
        if i not in a2:
            print(i)
    print('----')
    print("You are Not following back")
    for i in a2:
        if i not in b2:
            print(i)


def getfollowoing():
    driver.find_element_by_partial_link_text('following').click()
    sleep(1)
    scrollwindow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    # sleep(1)

    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scrollwindow)
    print(ht)
    following = scrollwindow.find_elements_by_class_name('Jv7Aj')
    following2 = scrollwindow.find_elements_by_tag_name('a')
    following3 = [name.text for name in following]
    following4 = [name.text for name in following2 if name.text != '']

    # print(following3)
    print(following4)
    with open(char_name + 'following.txt', 'w') as fp:
        for i in following4:
            fp.write(i + '\n')
    with open(char_name + 'following2.txt', 'w') as fp:
        for i in following3:
            fp.write(i)


def getfollowers():
    driver.find_element_by_partial_link_text('followers').click()
    sleep(1)
    scrollwindow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    # sleep(1)

    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scrollwindow)
    print(ht)
    following = scrollwindow.find_elements_by_class_name('Jv7Aj')
    following2 = scrollwindow.find_elements_by_tag_name('a')
    following3 = [name.text for name in following]
    following4 = [name.text for name in following2 if name.text != '']

    # print(following3)
    print(following4)
    with open(char_name + 'followers.txt', 'w') as fp:
        for i in following4:
            fp.write(i + '\n')
    with open(char_name + 'followers2.txt', 'w') as fp:
        for i in following3:
            fp.write(i + '\n')


driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
driver.get("https://www.instagram.com")
char_name = input("For whom are you executing the script:")
with open('userandpass.txt') as fp:
    user = fp.readline()
    pas = fp.readline()
    user = user.strip()
    pas = pas.strip()
sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(user)
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pas)
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').submit()
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
# sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]').click()
sleep(3)

try:
    getfollowoing()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
    sleep(1)
    getfollowers()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
except:
    pass

get_diff()
