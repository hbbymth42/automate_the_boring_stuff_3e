import pyautogui, time

print('Starting Looking Busy Mouse Movement: Press Ctrl-C to Stop Program')

while True:
    try:
        pyautogui.move(3, 0, 0.5)
        time.sleep(10)
    except KeyboardInterrupt:
        print('Ended!')
        break