import time
import pyautogui

def loading_pause_def():
    time.sleep(load_pause)

print('сколько фото обрабоать?')
x_foto = int(input())

print('пауза для прогрузки в сек?')
load_pause = float(input())

print('выполние начнется через 10 сек')

time.sleep(10)  # пауза перед стартом

for i in range(x_foto):
    pyautogui.hotkey('ctrl', 'u')
    loading_pause_def()
    pyautogui.press('right')
    loading_pause_def()


