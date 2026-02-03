# zelium/js.py
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import JavascriptException, TimeoutException

class JS:    
    _driver: WebDriver = None

    @classmethod
    def set_driver(cls, driver: WebDriver):
        cls._driver = driver

    @classmethod
    def execute(cls, script: str, *args):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")
        try:
            return cls._driver.execute_script(script, *args)
        except JavascriptException as e:
            print(f"[Error JS] {e}")
            return None

    # ─────────────────────────────
    # Sub funciones predeterminadas
    # ─────────────────────────────
    @classmethod
    def quitar_readonly(cls, xpath: str):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")
        try:
            elemento = cls._driver.find_element(By.XPATH, xpath)
            cls._driver.execute_script("arguments[0].removeAttribute('readonly')", elemento)
        except NoSuchElementException:
            print(f"[Advertencia] No se encontró el elemento con XPath: {xpath}")
        except JavascriptException as e:
            print(f"[Error] No se pudo eliminar el atributo 'readonly': {e}")
    
    @classmethod
    def set_value(cls, xpath: str, value):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")
        try:
            elemento = cls._driver.find_element(By.XPATH, xpath)
            cls._driver.execute_script("arguments[0].value = arguments[1];", elemento, value)
        except NoSuchElementException:
            print(f"[Advertencia] No se encontró el elemento con XPath: {xpath}")
        except JavascriptException as e:
            print(f"[Error] No se pudo establecer el valor: {e}")

    @classmethod
    def establecer_fecha(cls, xpath: str, valor: str):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")
        try:
            elemento = cls._driver.find_element(By.XPATH, xpath)
            cls._driver.execute_script("arguments[0].removeAttribute('readonly')", elemento)
            cls._driver.execute_script("arguments[0].value = arguments[1];", elemento, valor)
            cls._driver.execute_script(
                "arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", elemento
            )
        except NoSuchElementException:
            print(f"[Advertencia] No se encontró el elemento con XPath: {xpath}")
        except JavascriptException as e:
            print(f"[Error] No se pudo establecer la fecha: {e}")

    @classmethod
    def agregar_clase_valid(cls, xpath=None, xpaths=None, timeout=5):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")

        if not xpaths and not xpath:
            print("[Error] agregar_clase_valid: No se proporcionó ni 'xpath' ni 'xpaths'.")
            return 0

        if xpaths is None:
            xpaths = [xpath]

        if not isinstance(xpaths, (list, tuple)):
            print(f"[Error] agregar_clase_valid: 'xpaths' no es iterable ({type(xpaths)})")
            return 0

        modificados = 0
        js = "if (arguments[0]) { arguments[0].classList.add('valid'); return true; } return false;"

        for xp in xpaths:
            try:
                elemento = WebDriverWait(cls._driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xp))
                )
                result = cls._driver.execute_script(js, elemento)
                if result:
                    modificados += 1
            except TimeoutException:
                print(f"[Advertencia] No se encontró el elemento con XPath (timeout {timeout}s): {xp}")
            except JavascriptException as e:
                print(f"[Error JS en {xp}] {e}")
            except Exception as e:
                print(f"[Error inesperado en {xp}] {type(e).__name__}: {e}")

        return modificados
    
    @classmethod
    def scroll(cls, valor):
        if cls._driver is None:
            raise RuntimeError("Driver no asignado. Usa JS.set_driver(driver)")
        try:
            cls._driver.execute_script(f"window.scrollBy(0, {valor});")

        except Exception as e:
            print(e)
        except JavascriptException as e:
            print(f"[Error JS] No se pudo hacer scroll: {e}")
