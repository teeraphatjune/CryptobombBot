import pyautogui
import time
timeout = 5   # [seconds]
# timeout_start = time.time()

def login():
    conpos = pyautogui.locateAllOnScreen("./resources/connect.png"
    , confidence=0.99)
    # for pos in conpos:
    if conpos is not None:
        for i in conpos:
            pyautogui.doubleClick(i, interval=0.3)
            extendsign()
            sign()
            if isLobby():
                wakeup()
        time.sleep(1)

def sign(): # PRIVATE
    while time.time() < time.time() + timeout:
        sign = pyautogui.locateOnScreen("./resources/sign.png"
        , confidence=0.95)
        if sign is not None:
            pyautogui.click(sign)
            time.sleep(3)
            break

def treasure_h():
    while time.time() < time.time() + timeout:
        pos = pyautogui.locateOnScreen("./resources/treasure.png"
        , confidence=0.97)
        if pos:
            pyautogui.doubleClick(pos, interval=0.3)
            break
        time.sleep(3)

def extendsign(): # PRIVATE
    while time.time() < time.time() + timeout:
        time.sleep(3)      
        noti = pyautogui.locateOnScreen("./resources/mmnt.png"
        , confidence=0.95)
        if noti is not None:
            pyautogui.doubleClick(noti)
            return True

def wakeup():
    while time.time() < time.time() + timeout:
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
    while time.time() < time.time() + timeout:
        pos_wakeall = pyautogui.locateOnScreen("./resources/wakeall.png"
        , confidence=0.9)
        if pos_wakeall is not None:
            pyautogui.doubleClick(pos_wakeall, interval=0.3)
            break
        time.sleep(3)
    while time.time() < time.time() + timeout:
        pos_close = pyautogui.locateOnScreen("./resources/heroes_close.png"
        , confidence=0.97)
        if pos_close is not None:
            pyautogui.click(pos_close, clicks=2, interval=0.75)
            treasure_h()
        break
    time.sleep(3)

def sleepall():
    while time.time() < time.time() + timeout:
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
    while time.time() < time.time() + 15:
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