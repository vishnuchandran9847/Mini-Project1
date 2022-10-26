import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\chrome23\\chromedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
rad2=driver.find_element(by=By.ID,value="product_550").is_selected()
print(rad2)
rad2=driver.find_element(by=By.ID,value="product_550").click()
firstname=driver.find_element(by=By.ID,value="travname").send_keys("vishnu")
lastname=driver.find_element(by=By.ID,value="travlastname").send_keys("chandran")
additionalinformation=driver.find_element(by=By.NAME,value="order_comments").send_keys("2 black bags and 1 side hand bag")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.find_element(by=By.ID,value="dob")
#driver.find_element(by=By.XPATH,value="//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[4]/a").click()
gender=driver.find_element(by=By.NAME,value="sex").click()
addpassenger=driver.find_element(by=By.NAME,value="addmorepax").click()
se=Select(driver.find_element(by=By.ID,value="addpaxno"))
se.select_by_visible_text("add 1 more passenger (100%)")
time.sleep(2)
se.select_by_index(0)
triptype=driver.find_element(by=By.ID,value="traveltype_2").click()
fromcity=driver.find_element(by=By.ID,value="fromcity").send_keys("kozhikkode")
tocity=driver.find_element(by=By.ID,value="tocity").send_keys("Dubai")
deptime=driver.find_element(by=By.XPATH,value="//*[@id='departon']").click()
returndate=driver.find_element(by=By.ID,value="returndate").click()
additionalnotes=driver.find_element(by=By.ID,value="notes").send_keys("it's a very useful app and more easy and comfortable")
sel=Select(driver.find_element(by=By.ID,value="reasondummy"))
sel.select_by_visible_text("Prank a friend")
receivedummyticket=driver.find_element(by=By.NAME,value="deliverymethod").click()
#Billing details
billingname=driver.find_element(by=By.ID,value="billname").send_keys("Indigo")
phone=driver.find_element(by=By.ID,value="billing_phone").send_keys("9834255363")
emailaddrees=driver.find_element(by=By.NAME,value="billing_email").send_keys("vishnu123@gmail.com")
sel=Select(driver.find_element(by=By.ID,value="billing_country"))
sel.select_by_visible_text("India")
streetname=driver.find_element(by=By.ID,value="billing_address_1").send_keys("french colony in pondi")
apartname=driver.find_element(by=By.ID,value="billing_address_2").send_keys("rockhose no22,french colony")
towncity=driver.find_element(by=By.ID,value="billing_city").send_keys("tamilnadu")
sel=Select(driver.find_element(by=By.ID,value="billing_state"))
sel.select_by_visible_text("Assam")
pincode=driver.find_element(by=By.NAME,value="billing_postcode").send_keys("676503")
placeorder=driver.find_element(by=By.CSS_SELECTOR,value="button#place_order").click()







