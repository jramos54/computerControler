import pygetwindow as gw
import pyautogui
import time

def work_time(seconds):
    hours=seconds//3600
    minutes=(seconds%3600)//60
    second=seconds%60
    return f"{int(hours):02}:{int(minutes):02}:{second:.0f}"
    

def windows_navigate():
    
    pyautogui.keyDown('alt')
    time.sleep(1)
    windows=gw.getAllTitles()
    for window in windows:
        pyautogui.press('tab')
        time.sleep(1)
    pyautogui.keyUp('alt')
    
    
def window_select(title):
    
    for window in gw.getWindowsWithTitle(title):
        if title.lower() in window.title.lower():
            window.activate()
            time.sleep(1)
            window.maximize()
            break
    

def postman_work():
    
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(5)
    for i in range(7):
        mouse_movement()
    
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(15)
    for i in range(7):
        mouse_movement()
 
    
def mouse_movement():
    width_screen, heigth_screen = pyautogui.size()
    active_window = pyautogui.getActiveWindow()
    
    if active_window:
        center_x = active_window.left + active_window.width // 2
        center_y = active_window.top + active_window.height // 2

    pyautogui.moveTo(center_x, center_y,duration=2)
    time.sleep(2)
    
    point1=(center_x-width_screen//3,center_y+heigth_screen//3)
    point2=(center_x+1*(width_screen//3),center_y+heigth_screen//3)
    point3=(center_x-1*(width_screen//3),center_y-1*(heigth_screen//3))
    point4=(center_x+1*(width_screen//3),center_y-1*(heigth_screen//3))
    
    pyautogui.moveTo(point1[0], point1[1],duration=2)
    time.sleep(2)
    pyautogui.moveTo(point2[0], point2[1],duration=2)
    time.sleep(2)
    pyautogui.moveTo(point3[0], point3[1],duration=2)
    time.sleep(2)
    pyautogui.moveTo(point4[0], point4[1],duration=2)
    time.sleep(2)
 

def write_vscode():
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)  

    input_path="codigo.txt"
    with open(input_path, 'r') as archivo:
        codigo = archivo.readlines()
    
    for line in codigo:
        line=line.replace('\t',' '*4)
        if line != '\n':
            if line.endswith('\n'):
                line=line[:-1]
        else:
            line.replace('\n','')
        pyautogui.press('home')
        pyautogui.write(line, interval=0.5)
        pyautogui.press('esc')
        pyautogui.press('enter')
        

def chrome_work():
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    for i in range(6):
        mouse_movement()


def outlook_work():
    time.sleep(3)
    for i in range(6):
        mouse_movement()
        
        
def teams_work():
    time.sleep(3)
    for i in range(6):
        mouse_movement()


def power_shell():
    window_select('PowerShell')
    pyautogui.keyDown('alt')
    time.sleep(1)
    pyautogui.press('F4')
    time.sleep(1)
    pyautogui.keyUp('alt')


if __name__ == "__main__":
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = False
    
    start_time=time.time()
    
    for i in range(1):
        
        window_select('Google Chrome')
        chrome_work()
        window_select('KUSPIT')
        postman_work()
        window_select('Outlook')
        outlook_work()
        window_select('Teams')
        teams_work()

    end_time=time.time()
    
    print(work_time(end_time-start_time))
    
    power_shell()