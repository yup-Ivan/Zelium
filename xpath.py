from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    JavascriptException,
    TimeoutException,
    ElementNotInteractableException,
)
from .helpers import wait, find, scroll, js_click
import time


def exist(xpath, driver, timeout=5):
    try:
        find(xpath, driver, timeout)
        return True
    except TimeoutException:
        return False


def get_text(xpath, driver, timeout=5):
    try:
        elem = find(xpath, driver, timeout)
        return elem.text
    except TimeoutException:
        return None


def click(xpath, driver, timeout=5):
    try:
        elem = wait(
            driver,
            EC.element_to_be_clickable((By.XPATH, xpath)),
            timeout,
        )
        scroll(elem, driver)
        elem.click()
        return True

    except (TimeoutException, ElementNotInteractableException):
        try:
            elem = find(xpath, driver, timeout)
            scroll(elem, driver)
            js_click(elem, driver)
            return True
        except Exception:
            return False


def send_keys(xpath, value, driver, timeout=5):
    if value is None:
        return False

    try:
        elem = find(xpath, driver, timeout, visible=True)
        scroll(elem, driver)
        elem.clear()
        elem.send_keys(value)
        return True

    except (TimeoutException, ElementNotInteractableException):
        try:
            elem = find(xpath, driver, timeout)
            driver.execute_script(
                """
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
                arguments[0].dispatchEvent(new Event('change', {bubbles:true}));
                """,
                elem,
                value,
            )
            return True
        except Exception:
            return False


def select(xpath, buscar, driver, attr="value", timeout=5):
    try:
        elem = find(xpath, driver, timeout)
        scroll(elem, driver)

        sel = Select(elem)
        buscar = str(buscar)

        if attr == "value":
            sel.select_by_value(buscar)
        elif attr == "text":
            sel.select_by_visible_text(buscar)
        else:
            for option in sel.options:
                if option.get_attribute(attr) == buscar:
                    option.click()
                    break
            else:
                return False

        return True

    except Exception:
        return False


def force_select_combobox(input_xpath, option_text, driver, timeout=5):
    try:
        input_elem = find(input_xpath, driver, timeout)
        scroll(input_elem, driver)
        input_elem.click()

        option_xpath = (
            f"//li[@role='option' and normalize-space(text())='{option_text}']"
        )
        option_elem = find(option_xpath, driver, timeout)

        scroll(option_elem, driver)
        js_click(option_elem, driver)

        return True

    except Exception:
        return False


def clear(xpath, driver, timeout=5):
    try:
        elem = find(xpath, driver, timeout)
        elem.clear()
        return True
    except Exception:
        return False


def delDisable(xpath, driver, timeout=5):
    try:
        elem = find(xpath, driver, timeout)
        driver.execute_script(
            """
            arguments[0].removeAttribute('readonly');
            arguments[0].removeAttribute('disabled');
            try { arguments[0].readOnly = false; } catch(e) {}
            """,
            elem,
        )
        time.sleep(0.3)
        elem.click()
        return True

    except (TimeoutException, JavascriptException):
        return False
