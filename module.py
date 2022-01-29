import pyautogui
import time
timeout = 10   # [seconds]
timeout_start = time.time()

def locate_all(path, confidence=0.9, distance=10):
    distance = pow(distance, 2)
    elements = []
    for element in pyautogui.locateAllOnScreen(path, confidence=confidence):
        if all(map(lambda x: pow(element.left - x.left, 2) + pow(element.top - x.top, 2) > distance, elements)):
            elements.append(element)
    return elements

def setTime():
    global timeout_start
    timeout_start = time.time()

def login():
    conpos = pyautogui.locateAllOnScreen("./resources/connect.png"
    , confidence=0.99)
    # for pos in conpos:
    if conpos is not None:
        for i in conpos:
            if errorHandle():
                break
            pyautogui.doubleClick(i, interval=0.3)
            extendsign()
            sign()
            if isLobby():
                wakeup()
        time.sleep(1)

def sign(): # PRIVATE
    setTime()
    while time.time() < timeout_start + timeout:
        print("sign")
        sign = pyautogui.locateOnScreen("./resources/sign.png"
        , confidence=0.95)
        if sign is not None:
            pyautogui.click(sign)
            break
        time.sleep(1)
        

def treasure_h():
    setTime()
    while time.time() < timeout_start + timeout:
        if errorHandle():
            break
        pos = pyautogui.locateOnScreen("./resources/treasure.png"
        , confidence=0.9)
        if pos:
            pyautogui.doubleClick(pos, interval=0.3)
            break
        time.sleep(3)

def extendsign(): # PRIVATE
    setTime()
    while time.time() < timeout_start + timeout:
        print("extendsign")
        noti = pyautogui.locateOnScreen("./resources/mmnt.png"
        , confidence=0.95)
        if noti is not None:
            pyautogui.doubleClick(noti, interval=0.3)
            return True
        time.sleep(0.2)

def wakeup():
    setTime()
    while time.time() < timeout_start + timeout:
        print("wakeup")
        if errorHandle():
            break
        pos_heroes = pyautogui.locateOnScreen("./resources/heroes.png"
        , confidence=0.97)
        if pos_heroes is not None:
            pyautogui.doubleClick(pos_heroes, interval=0.3)
            break
        time.sleep(3)
    pos_sleepall = pyautogui.locateOnScreen("./resources/sleepall.png"
    , confidence=0.9)
    if pos_sleepall is not None:
        pyautogui.doubleClick(pos_sleepall, interval=0.3)

    setTime()
    while time.time() < timeout_start + timeout:
        print("wakeall")
        pos_wakeall = pyautogui.locateOnScreen("./resources/wakeall.png"
        , confidence=0.8)
        if pos_wakeall is not None:
            pyautogui.doubleClick(pos_wakeall, interval=0.3)
            break
        time.sleep(3)
    setTime()
    while time.time() < timeout_start + timeout:
        pos_close = pyautogui.locateOnScreen("./resources/heroes_close.png"
        , confidence=0.97)
        if pos_close is not None:
            pyautogui.click(pos_close, clicks=2, interval=0.75)
            treasure_h()
        break
    time.sleep(3)

def sleepall():
    setTime()
    while time.time() < timeout_start + timeout:
        pos_sleepall = pyautogui.locateOnScreen("./resources/sleepall.png"
        , confidence=0.97)
        if pos_sleepall:
            pyautogui.click(pos_sleepall)
            break
        time.sleep(3)

def resetwalk():
    pos_back = pyautogui.locateAllOnScreen("./resources/btn_back.png"
    , confidence=0.97)
    if pos_back is not None:
        for i in pos_back:
            pyautogui.doubleClick(i, interval=0.3)
            treasure_h()

def isLobby():
    setTime()
    while time.time() < timeout_start + 20:
        print("isLobby")
        pos_lobby = pyautogui.locateOnScreen("./resources/lobby.png"
        , confidence=0.97)
        if pos_lobby is not None:
            return True
        time.sleep(1)

def errorHandle():
    pos_error = pyautogui.locateAllOnScreen("./resources/error.png"
    , confidence=0.97)
    for i in pos_error:
        if pos_error is not None:
            pyautogui.doubleClick(i, interval=0.3)
            return True

def awake_while_playing():
    pos_back = pyautogui.locateAllOnScreen("./resources/btn_back.png"
    , confidence=0.97)
    if pos_back is not None:
        for i in pos_back:
            pyautogui.doubleClick(i, interval=0.3)
            wakeup()

def chk_treasure_h():
    pos = pyautogui.locateAllOnScreen("./resources/treasure.png"
    , confidence=0.97)
    if pos is not None:
        for i in pos:
            pyautogui.doubleClick(i, interval=0.3)

def chk_btn_close():
    pos_close = pyautogui.locateAllOnScreen("./resources/heroes_close.png"
    , confidence=0.97)
    if pos_close is not None:
        for i in pos_close:
            pyautogui.doubleClick(i, interval=0.3)