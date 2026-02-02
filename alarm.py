# Zelium/alarm.py
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver

class Alarm:
    _driver: WebDriver = None

    @classmethod
    def set_driver(cls, driver: WebDriver):
        cls._driver = driver

    @classmethod
    def _get_alert(cls):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa Zelium.alarm.set_driver(driver)")
        try:
            return cls._driver.switch_to.alert
        except NoAlertPresentException:
            return None

    @classmethod
    def accept(cls):
        alert = cls._get_alert()
        if alert:
            alert.accept()
            return True
        return False

    @classmethod
    def deny(cls):
        alert = cls._get_alert()
        if alert:
            alert.dismiss()
            return True
        return False

    @classmethod
    def delete(cls):
        alert = cls._get_alert()
        if alert:
            text = alert.text
            alert.accept()
            return text
        return None

    @classmethod
    def text(cls):
        alert = cls._get_alert()
        if alert:
            return alert.text
        return None
