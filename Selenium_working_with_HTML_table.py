from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Admin/Desktop/new%202.html")

rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
columns=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("The number of rows in the table are: ",rows)
print("The number of columns in the table are: ",columns)

element=driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]").text
print(element)

for r in range(2,rows+1):
    for c in range(1,columns+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="       ")
    print()


driver.close()
