from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template

keyboard_controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "mistral:7b-instruct-v0.2-q4_K_S",
    "keep_alive": "5m",
    "stream": False,
}

def fix_current_line():
    keyboard_controller.press(Key.cmd)
    keyboard_controller.press(Key.shift)
    keyboard_controller.press(Key.left)

    keyboard_controller.release(Key.cmd)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release(Key.left)

    fix_selection()

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

$text

Return only the corrected text, don't include a preamble.
"""
)

def fix_text(text: str):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT, json={"prompt": prompt, **OLLAMA_CONFIG}, headers={"Content-Type": "application/json"}, timeout=10)
    if response.status_code != 200:
        print("Error calling ollama model", response.status_code)
        return None
    return response.json()["response"].strip()

def fix_selection():
    with keyboard_controller.pressed(Key.cmd):
        keyboard_controller.tap("c")
    
    time.sleep(0.1)
    text = pyperclip.paste()
    
    if not text:
        return
    
    fixed_text = fix_text(text)
    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    with keyboard_controller.pressed(Key.cmd):
        keyboard_controller.tap("v")


def on_down():
    fix_current_line()

def on_up():
    fix_selection()

with keyboard.GlobalHotKeys({'<125>': on_down, '<126>': on_up }) as h:
    # Key.down.value = 55 and Key.up.value=56
    h.join()