from selenium.webdriver import Chrome
import time

driver=Chrome()
driver.get("http://www.msn.com")
driver.execute_script("window.open('http://www.facebook.com','new window')")
Handles=driver.window_handles
print(Handles, type(Handles))

for Handle in Handles:
    print(Handle)
driver.switch_to_window(Handles[1])
time.sleep(5)
driver.quit()
driver.s