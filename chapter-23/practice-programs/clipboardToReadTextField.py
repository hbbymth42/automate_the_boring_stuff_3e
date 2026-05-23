import pyautogui, pyperclip

editorWindow = pyautogui.getWindowsWithTitle('Notepad')[0]

editorWindowPosition = editorWindow.topleft

pyautogui.click(editorWindowPosition[0]+50, editorWindowPosition[1]+50)

pyautogui.hotkey('ctrl', 'a')

pyautogui.hotkey('ctrl', 'c')

print(pyperclip.paste())