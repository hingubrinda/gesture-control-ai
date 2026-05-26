import pyautogui
import os
import time

last_screenshot_time = 0


def volume_up():
    os.system(
        "osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'"
    )


def volume_down():
    os.system(
        "osascript -e 'set volume output volume ((output volume of (get volume settings)) - 10)'"
    )


def take_screenshot():

    global last_screenshot_time

    current_time = time.time()

    # 3 second cooldown
    if current_time - last_screenshot_time > 3:
        time.sleep(1)

        screenshot = pyautogui.screenshot()

        filename = f"screenshots/screenshot_{int(current_time)}.png"

        screenshot.save(filename)

        print(f"Saved: {filename}")

        last_screenshot_time = current_time

        return True

    return False