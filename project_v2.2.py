import pyautogui
import keyboard as keyb
import time
import pyclip
import threading
from pynput import mouse
from pynput.keyboard import Key, Listener
from pynput import keyboard



#отвечают за код(не изменяемо) и за время(изменяемо) соответственно
CODE = []
TIMES = []

def on_press(key):
    keyboard_releaser(key)

def on_release(key):
    if key == Key.f12:
        CODE.pop()
        TIMES.pop()
        return False

col = 1
def on_scroll(x, y, dx, dy):
    global col
    global CODE
    global TIMES
    global vremya
    global key_vremya
    if key_vremya == False:
        vremya = time.time() - vremya
    if dy < 0:
        #down
        CODE.append(f"pyautogui.moveTo({x}, {y})\ntime.sleep({vremya})\nmouse.wheel(-1)\n")
        TIMES.append("#\n")

        #проверка на повторения
        ch = f")\nmouse.wheel(-"
        try:
            if (ch in CODE[-1]) and (ch in CODE[-2]) and col < 9:
                CODE.pop()
                TIMES.pop()
                col = int(CODE[-1][-3]) + 1
                CODE[-1] = CODE[-1][:-3]
                CODE[-1] = CODE[-1] + str(col) + ")\n"
            else:
                col = 1
        except:
            pass
    else:
        #up
        CODE.append(f"pyautogui.moveTo({x}, {y})\ntime.sleep({vremya})\nmouse.wheel(+1)\n")
        TIMES.append("#\n")

        # проверка на повторения
        ch = f")\nmouse.wheel(+"
        try:
            if (ch in CODE[-1]) and (ch in CODE[-2]) and col < 9:
                CODE.pop()
                TIMES.pop()
                col = int(CODE[-1][-3]) + 1
                CODE[-1] = CODE[-1][:-3]
                CODE[-1] = CODE[-1] + str(col) + ")\n"
            else:
                col = 1
        except:
            pass
    if key_vremya == False:
        vremya = time.time()


def double_click_cheaker(x, y):
    global start_time
    time.sleep(0.31)
    if (time.time() - start_time) < 0.3 and (x == pyautogui.position()[0] and y == pyautogui.position()[1]):
        CODE.pop()
        TIMES.pop()
        CODE.pop()
        TIMES.pop()
        double_click_bind(x, y)

start_time = 0

def on_click(x, y, button, pressed):
    global start_time
    if pressed and button == mouse.Button.left:
        start_time = time.time()
        threading.Thread(target=click_bind, args=(x, y, )).start()
        threading.Thread(target=double_click_cheaker, args=(x, y, )).start()
    if pressed and button == mouse.Button.right:
        start_time = time.time()
        threading.Thread(target=right_click_bind, args=(x, y,)).start()
    if keyb.is_pressed('F12'):
        return False


key_vremya = True


def open_idle():
    global vremya
    global key_vremya

    #открываем консоль
    # pyautogui.moveTo(120, 1063)
    # pyautogui.click()
    # pyautogui.write('cmd')
    # pyautogui.moveTo(123, 504)
    # pyautogui.click()
    # time.sleep(0.5)

    #устанавливаем необходимые библиотеки
    # pyautogui.write("pip install pyautogui")
    # keyb.send('enter')
    # time.sleep(9)
    # pyautogui.write("pip install keyboard")
    # keyb.send('enter')
    # time.sleep(3)


    #открываем Pyton
    with open(f"{path}{name}.py", "w") as best_file:

        # прописываем необходимый минимум кода
        best_file.write("import pyautogui\n")
        best_file.write('import time\n')
        best_file.write('import mouse\n')
        best_file.write('import keyboard as keyb\n\n\n')
        best_file.write('pyautogui.moveTo(1900, 20)\n')
        best_file.write('pyautogui.click()\n')
        best_file.write(f"for i in range(0, {fori}):\n")

    if vremya == 0:
        vremya = time.time()
        key_vremya = False


def right_click_bind(x, y):
    global vremya
    global key_vremya
    if key_vremya == False:
        vremya = time.time() - vremya
    CODE.append(f"pyautogui.moveTo({x}, {y})\npyautogui.rightClick()\n")
    TIMES.append(f"time.sleep({vremya})\n")
    if key_vremya == False:
        vremya = time.time()

def click_bind(x, y):
    global vremya
    global key_vremya
    if key_vremya == False:
        vremya = time.time() - vremya
    CODE.append(f"pyautogui.moveTo({x}, {y})\npyautogui.click()\n")
    TIMES.append(f"time.sleep({vremya})\n")
    if key_vremya == False:
        vremya = time.time()


def double_click_bind(x, y):
    global vremya
    global key_vremya
    if key_vremya == False:
        vremya = time.time() - vremya
    CODE.append(f"pyautogui.moveTo({x}, {y})\npyautogui.doubleClick()\n")
    TIMES.append(f"time.sleep({vremya})\n")
    if key_vremya == False:
        vremya = time.time()


def keyboard_releaser(key):
    global vremya
    global key_vremya
    if key_vremya == False:
        vremya = time.time() - vremya

    # Проверка на буквенные клавиши и остальные клавиши
    ch = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    if str(key)[1:-1] in ch:
        CODE.append(f"pyautogui.write('{str(key)[1:-1]}')\n")
        TIMES.append("#\n")
    else:
        new_key = str(key)[4:]
        CODE.append(f"pyautogui.press('{new_key}')\n")
        TIMES.append(f"time.sleep({vremya})\n")

    #Объеденяем буквенные клавиши, чтобы не тратить место
    ch1 = "pyautogui.write("
    try:
        if ch1 in CODE[-1] and ch1 in CODE[-2]:
            CODE.pop()
            TIMES.pop()
            CODE[-1] = CODE[-1][:17] + CODE[-1][17:-3] + str(key)[1:-1] + CODE[-1][-3:]
    except:
        pass
    if key_vremya == False:
        vremya = time.time()


#Эта функция пока не используется
def copy_past():
    time.sleep(0.1)
    paste = pyclip.paste().decode("utf-8")
    paste1 = ""
    for i in range(0, len(paste)):
        if "\'" in paste[i]:
            paste1 += '"'
        else:
            paste1 += paste[i]
    return paste1


def end():
    pyautogui.click()
    pyautogui.press('ctrl')
    pyautogui.moveTo(120, 1063)
    pyautogui.click()
    pyautogui.write('IDLE (Python')
    time.sleep(1)
    pyautogui.moveTo(123, 504)
    pyautogui.click()
    time.sleep(1)
    keyb.send('ctrl + O')
    time.sleep(0.5)
    keyb.write(f"{path}{name}.py")
    keyb.send('enter')
    time.sleep(3)
    CODE.pop()
    TIMES.pop()

    time.sleep(1)
    keyb.send('win + up')
    time.sleep(3)
    for i in range(10):
        keyb.send('down')
    m = 0

    #записываем код
    keyb.send('tab')
    for i in CODE:
        pyautogui.write(TIMES[m])
        pyautogui.write(CODE[m])
        m += 1
    # pyautogui.moveTo(1900, 20)
    # pyautogui.click()
    # keyb.send('enter')



vremya = input("Введите временной промежуток между выполнениями действий в секундах: ")
if vremya == "" or float(vremya) <= 0:
    vremya = 0
fori = input("Введите количество повторений программы: ")
if fori == "":
    fori = 1
else:
    fori = int(fori)
    if fori < 1:
        fori = 1
name = input("Введите название программы: ")
if name == "":
    name = 'script'
path = input("Введите путь, по которому будет создана программа: ")
if path == "":
    path = "C:\\Users\\Res\\OneDrive\\Рабочий стол\\школа3\\pg_script\\"
else:
    for i in path:
        if '/' in i:
            path = path.split('/')
            path = "\\".join(path)
            break
open_idle()
keyb.add_hotkey('F12', end)
with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        keyb.wait('F12')
        listener.join()
