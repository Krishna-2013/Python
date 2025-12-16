import pyautogui
import pyperclip
import time

# Small delay before starting (so you can switch windows if needed)
time.sleep(2)

# Step 1: Click on the whatsapp icon at (1260, 1041)
pyautogui.click(1042, 1040)
time.sleep(1)  # wait for the app to open/respond

# Step 2: Drag from (664, 213) to (675, 915) to select the text
pyautogui.moveTo(745, 260)
pyautogui.dragTo(1417,916, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy (Ctrl + C)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Step 4: Get text from clipboard
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)
