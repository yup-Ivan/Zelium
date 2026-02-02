# ZELIUM

**ZELIUM** is a web automation framework based on **Selenium**, written in **Python**, designed to **simplify, standardize, and accelerate** the creation of web automation scripts.

It is designed to:
- Reduce repetitive code
- Centralize common patterns (waits, scrolls, JS fallbacks…)
- Provide a clear and expressive API (in Spanish and English)
- Make maintenance of complex automation scripts easier

---

## 👤 Author

- 💻 GitHub: https://github.com/yup-Ivan

---

## 🎯 Main Goals

- 🧠 Intelligent abstraction over Selenium  
- 🔁 Reuse of common logic via helpers  
- 🛡️ Robustness against dynamic elements (React, Vue, etc.)  
- 🧩 Clean, readable, and consistent API  
- 🌍 Multilanguage support (aliases in Spanish / English)

---

## 📁 Project Structure

```text
Zelium/
├── __init__.py   # Public API of the framework (exports and aliases)
├── alarm.py      # Handling browser alerts, confirms, and prompts
├── config.py     # Global initialization and configuration (driver, options…)
├── helpers.py    # Internal helpers (wait, find, scroll, js_click, etc.)
├── js.py         # JavaScript utilities (scroll, set_value, remove readonly…)
├── tools.py      # Reusable helper functions
└── xpath.py      # XPath element actions (click, send_keys, select…)
