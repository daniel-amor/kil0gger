from os import replace
import keyboard
from datetime import datetime
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
recording = True
keys = []
while recording:
    event = keyboard.read_event()
    if event.event_type == "down":
        if keyboard.is_pressed("shift") and keyboard.is_pressed("f") and keyboard.is_pressed("control"):
            recording = False
        else:
            keys.append(event.name)
def custom_print(message_to_print, log_file='final_output.json'):
    with open(log_file, 'a') as of:
        of.write(message_to_print + '\n')
    return message_to_print
keys.append(f",\"reading Time:{currentTime}\"")
keys = [key for key in keys if key not in ["shift", "ctrl", "F"]]
print(custom_print(str(keys)))
with open('final_output.json', 'r') as rem:
    final = rem.readlines()
    cleaned_lines = [line.replace("'", "").replace(",", "").strip() +"\n" for line in final]
with open('final_output.json', 'w') as rem:
    rem.writelines(cleaned_lines)


