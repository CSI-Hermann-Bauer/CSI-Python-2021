from selenium import webdriver
driver =webdriver.Firefox(executable_path=r'/Users/hermannbauer/Downloads/geckodriver')

portals = ['https://apply.purdue.edu/account/login?r=https%3a%2f%2fapply.purdue.edu%2fapply%2fstatus%3f_ga%3d2.54570283.1621315557.1648482449-1620707212.1648063246','https://pathway.wustl.edu/account/login']
for links in portals:
    driver.get(links)
    email = driver.find_element_by_id("email")
    email.send_keys("22-106@sanignacio.pr")
    password = driver.find_element_by_id("password")
    password.send_keys("Hbmontalvo1!")
    driver.find_element_by_class_name('default').click()
#login = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/main/div/form/table/tbody/tr/td[1]/div/button")
#login.click()