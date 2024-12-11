import pyautogui, keyboard
import subprocess
import time, os, random

def work_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    second = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{second:.0f}"

def window_select(title):
    print(f"Selecting {title} window")
    cmd = f'osascript -e \'activate application "{title}"\''
    subprocess.call(cmd, shell=True)

def postman_work():
    window_select("Postman")
    # time.sleep(60)

    for i in range(10):
        pyautogui.keyDown('command')
        pyautogui.keyDown('shift')
        pyautogui.press('{')
        pyautogui.keyUp('command')
        pyautogui.keyUp('shift')
        # keyboard.press_and_release("shift+command,42")
        time.sleep(60)

def mouse_movement():
    x=[125,375,750,1000]
    y=[250,500,750,1000]
    width,length=pyautogui.size()
    xpos=random.choice(x)
    ypos=random.choice(y)
    pyautogui.moveTo(xpos,ypos)
    time.sleep(60)


def chrome_work():
    window_select("Google Chrome")
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    for i in range(10):
        mouse_movement()

def visual_work():
    # keys=["(",'"',"'","{","["]
    window_select("Visual Studio Code")
    pyautogui.keyDown("command")
    pyautogui.press("n")
    pyautogui.keyUp("command")

    time.sleep(5)

    directorio="codes"
    archivos=os.listdir(directorio)
    archivo=random.choice(archivos)

    ruta=os.path.join(directorio,archivo)

    with open(ruta,'r',encoding='utf-8') as file:
        contenido=file.read()

    lines=contenido.split('\n')

    for line in lines:
        # pyautogui.hotkey('command', 'left')
        
        line.replace("\t"," "*4)

        if line != '\n':
            if line.endswith('\n'):
                line=line[:-1]
        else:
            line.replace('\n','')

        keyboard.press_and_release('command + left')
        time.sleep(2)
        for _ in line:
            keyboard.write(_)
            time.sleep(.25)
        keyboard.press_and_release('enter')
        keyboard.press_and_release('command + left')
        time.sleep(5)

def terminal_work():
    window_select("Terminal")
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    for i in range(10):
        mouse_movement()

def docker_work():
    window_select("Docker Desktop")
    for i in range(10):
        mouse_movement()
        time.sleep(60)

def finder_work():
    window_select("Finder")
    for i in range(5):
        mouse_movement()
        time.sleep(60)


if __name__ == "__main__":

    time.sleep(30)
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = False
    
    start_time = time.time()
    for i in range(1):
        print(f"Iteracion {i}")
        chrome_work()
        time.sleep(60)
        postman_work()
        time.sleep(60)
        finder_work()
        time.sleep(60)
        visual_work()
        time.sleep(60)
        terminal_work()
        time.sleep(60)
        docker_work()
        time.sleep(60)
        chrome_work()
        time.sleep(60)
        # visual_work()
        postman_work()
        time.sleep(60)
        terminal_work()
        time.sleep(60)
        finder_work()
        time.sleep(60)
        postman_work()

    end_time = time.time()
    
    print(work_time(end_time - start_time))
            
