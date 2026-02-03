import zelium
import time

driver = zelium.start()
zelium.open("https://example.com/", driver)
zelium.click("/html/body/div/p[2]/a", driver)
time.sleep(5)
driver.quit()
