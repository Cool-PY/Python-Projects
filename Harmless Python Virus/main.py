import pyautogui

a = pyautogui.confirm(text="Do you want to download this game for free! Tap on OK to continue.", title="Do you want to continue", buttons=['OK', 'Cancel'])

if a == 'Cancel':
    print(a)
    while True:
        pyautogui.confirm(text="You are hacked more!", title="You are hacked more!", buttons=['OK', 'Cancel'])

else:
    print(a)
    for i in range(21):
        pyautogui.confirm(text="You are hacked more!", title="You are hacked more!", buttons=['OK', 'Cancel'])
