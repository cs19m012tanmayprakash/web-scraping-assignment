from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

t1=input("eneter the topic which you want to learn: ")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.ftuudemy.com/")
#email = driver.find_element_by_id("login_field")
#email.send_keys("CS19M007@iittp.ac.in")
#password = driver.find_element_by_id("password")
#password.send_keys("password")
#sign = driver.find_element_by_name("commit")
#sign.click()
search=driver.find_element_by_name("s")
search.send_keys(t1)
search.send_keys(Keys.ENTER)

f = open("course_descriptor.txt", "w")
for var in range(1,8):

    title = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/article["+str(var)+"]/div[2]/div/header/div/h2/a")
    description=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/article["+str(var)+"]/div[2]/div/div[1]")
    print("title: "+ title.text)
    print("description: "+ description.text)
    print("\n")
    f.write("course Name : ")
    f.write(title.text)
    f.write("\ndescripton : ")
    f.write(description.text)
    f.write("\n\n")
    
    
f.close()