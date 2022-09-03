from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://shubhangini22.github.io/verbose-giggle/")
driver.close()
driver.quit()
print(driver.title)

