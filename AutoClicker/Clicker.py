import mouse
import keyboard
import time

right_click = False;

button = input("Введите клавишу: ")
delay = input("Введите задержку: ")

while True:
	time.sleep(float(delay))
	if keyboard.is_pressed(button):
		mouse.click("left")