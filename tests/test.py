import Zelium
import time

driver = Zelium.start()

Zelium.open("http://127.0.0.1:5000", driver)
Zelium.alarm.accept()
Zelium.js.quitar_readonly("//input[@id='fecha']")
Zelium.js.set_value("//input[@id='nombre']", "Iván")
Zelium.js.scroll(300)
driver.quit()
