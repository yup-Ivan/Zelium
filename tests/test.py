import zelium
import time

driver = zelium.start()

zelium.open("http://127.0.0.1:5000", driver)
zelium.alarm.accept()
zelium.js.quitar_readonly("//input[@id='date']")
zelium.js.set_value("//input[@id='name']", "NAME")
zelium.js.scroll(300)
driver.quit()
