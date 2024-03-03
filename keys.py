import keyboard
import json

key_list = [{'lap': 0}]
lap = 0

def on_key_release(event):
    global lap
    global key_list
    key = event.name
    key_counts = key_list[lap]
    if key == 'f5':
        lap += 1
        key_list.append({'lap': lap})
    elif key.capitalize() in ['W', 'A', 'S', 'D']:
        key = key.capitalize();
        key_counts[key] = key_counts.get(key, 0) + 1
        print(f"Key '{key}' pressed. Total count: {key_counts[key]}")

        with open('key_counts.json', 'w') as file:
            json.dump(key_list, file, indent=2)

keyboard.on_release(on_key_release)

try:
    keyboard.wait()
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()