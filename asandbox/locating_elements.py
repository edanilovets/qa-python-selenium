from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:80/addressbook/")
driver.find_element_by_name("user").send_keys("admin")
driver.find_element_by_name("pass").send_keys("secret")
driver.find_element_by_css_selector("input[type=submit]").click()
driver.find_element_by_link_text("groups").click()
groups = driver.find_elements_by_class_name("group")

print(groups)


driver.close()
