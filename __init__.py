# zelium/__init__.py
from .js import JS
from .alarm import Alarm
from .tools import open
from .config import start
from .xpath import (
    exist, get_text, click, send_keys,
    select, force_select_combobox, clear,
    delDisable,
)

__version__ = "0.1.6"

# ─────────────────────────────
# Alias (multi-idioma / semánticos)
# ─────────────────────────────
JavaScript = JS
Alarma = Alarm

empezar = start
abrir = open

existe = exist
obtener_texto = get_text
pulsar = click
enviar = send_keys
seleccionar = select
forzar_combobox = force_select_combobox
limpiar = clear
quitar_disable = delDisable

# ─────────────────────────────
# API
# ─────────────────────────────
__all__ = [
    "JS", "JavaScript",
    "Alarm", "Alarma",
    "start", "empezar",
    "open", "abrir",
    "exist", "existe",
    "get_text", "obtener_texto",
    "click", "pulsar",
    "send_keys", "enviar",
    "select", "seleccionar",
    "force_select_combobox", "forzar_combobox",
    "clear", "limpiar",
    "noDisable", "quitar_disable",
    "alarm", "js",
]

# ─────────────────────────────
# Instancias
# ─────────────────────────────
alarm = Alarm
js = JS
