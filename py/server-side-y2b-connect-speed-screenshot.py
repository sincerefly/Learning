#!/bin/env python
# -*- coding: utf-8 -*-

# use: https://blog.ishell.me/a/you2be-connection-speed.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

profile = webdriver.FirefoxProfile()
profile.add_extension('/root/downloads/addon-328839-latest.xpi')
profile.set_preference("extensions.y2bautohd.currentVersion", "49.1")

driver = webdriver.Firefox(firefox_profile=profile)

#driver = webdriver.Firefox()


driver.get('https://www.youtube.com/watch?v=TmDKbUrSYxQ')
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

driver.get('https://www.youtube.com/watch?v=TmDKbUrSYxQ')
time.sleep(30)

ele = driver.find_element_by_id('movie_player')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(ele, 100, 100).context_click().perform()
time.sleep(3)

driver.find_element_by_xpath('//div[text() = "Stats for nerds"]').click()
time.sleep(3)

img_name = str(time.time())[0:10] + '.png'
driver.save_screenshot('/root/downloads/'+img_name)

