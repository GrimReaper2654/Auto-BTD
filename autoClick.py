import pyautogui
import time
from playsound import playsound

if (True): # use pytesseract for image recognition (used for harder modes) (requires download)
    from PIL import Image
    import pytesseract
    # update according to your installation
    pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def placeTower(pos, key):
    pyautogui.click(scaleCoords(400, 400)) # handle levelup
    time.sleep(0.1)
    pyautogui.click(scaleCoords(400, 400))
    time.sleep(0.1)
    pyautogui.typewrite(key)
    time.sleep(0.1)
    pyautogui.click(scaleCoords(pos[0], pos[1]))
    time.sleep(0.1)

def selectTower(pos):
    pyautogui.click(scaleCoords(400, 400)) # handle levelup
    time.sleep(0.1)
    pyautogui.click(scaleCoords(400, 400))
    time.sleep(0.1)
    pyautogui.click(scaleCoords(pos[0], pos[1]))
    time.sleep(0.5)

def upgradeTower(pos, path):
    pyautogui.click(scaleCoords(400, 400)) # handle levelup
    time.sleep(0.1)
    pyautogui.click(scaleCoords(400, 400))
    time.sleep(0.1)
    pyautogui.click(scaleCoords(pos[0], pos[1]))
    time.sleep(0.1)
    if path == 1:
        key = ','
    elif path == 2:
        key = '.'
    elif path == 3:
        key = '/'
    elif path == 4:
        key = ''
        pyautogui.press('left')
    elif path == 5:
        key = ''
        pyautogui.press('right')
    pyautogui.typewrite(key)
    time.sleep(0.1)
    pyautogui.press('esc')

def txtFromImg(path):
    img = Image.open(path)
    txt = pytesseract.image_to_string(img)
    procesedTxt = ''
    for char in txt:
        if char.isnumeric():
            procesedTxt += char
    print(f'IMAGE RECOGNITION: raw: {txt}, processed: {procesedTxt}')
    return procesedTxt

def getMoney():
    upperLeftX, upperLeftY = scaleCoords(167,300)
    X, Y = scaleCoords(180,45)
    img = pyautogui.screenshot('money.png', region=(int(upperLeftX), int(upperLeftY), int(X), int(Y)))
    time.sleep(0.25)
    txt = pytesseract.image_to_string(img)
    procesedTxt = ''
    for char in txt:
        if char.isnumeric():
            procesedTxt += char
    print(f'IMAGE RECOGNITION: raw: {txt}, processed: {procesedTxt}')
    return procesedTxt

def canUpgrade(path): # no paragon support
    p1XL, p1YL = scaleCoords(117,532)
    p2XL, p2YL = scaleCoords(117,605)
    p3XL, p3YL = scaleCoords(117,680)
    p1XR, p1YR = scaleCoords(690,532)
    p2XR, p2YR = scaleCoords(690,605)
    p3XR, p3YR = scaleCoords(690,680)
    if path == 1:
        L = pyautogui.screenshot(region=(int(p1XL), int(p1YL), 2, 2))
        R = pyautogui.screenshot(region=(int(p1XR), int(p1YR), 2, 2))
        time.sleep(0.2)
        if L.getcolors() == [(2, (127, 219, 66, 255)), (2, (126, 219, 66, 255))] or R.getcolors() == [(2, (127, 219, 66, 255)), (2, (126, 219, 66, 255))]:
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    elif path == 2:
        L = pyautogui.screenshot(region=(int(p2XL), int(p2YL), 2, 2))
        R = pyautogui.screenshot(region=(int(p2XR), int(p2YR), 2, 2))
        time.sleep(0.2)
        if L.getcolors() == [(2, (128, 220, 67, 255)), (2, (127, 220, 67, 255))] or R.getcolors() == [(2, (128, 220, 67, 255)), (2, (127, 220, 67, 255))]:
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    elif path == 3:
        L = pyautogui.screenshot(region=(int(p3XL), int(p3YL), 2, 2))
        R = pyautogui.screenshot(region=(int(p3XR), int(p3YR), 2, 2))
        time.sleep(0.2)
        print(L.getcolors())
        if L.getcolors() == [(2, (126, 218, 66, 255)), (2, (125, 218, 66, 255))] or R.getcolors() == [(2, (126, 218, 66, 255)), (2, (125, 218, 66, 255))]:
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    else:
        print('change targeting detected')
        return True

def checkComplete():
    upperLeftX, upperLeftY = scaleCoords(355,610)
    X, Y = scaleCoords(180,60)
    img = pyautogui.screenshot('complete.png', region=(int(upperLeftX), int(upperLeftY), int(X), int(Y)))
    time.sleep(0.5)
    txt = pytesseract.image_to_string(img)
    print(f'IMAGE RECOGNITION: {txt}')
    if 'insta' in txt.lower():
        return True
    return False

def scaleCoords(x, y):
    # your btd6 display size (change to fit your screen)
    upperLeft = [0,295]
    lowerRight = [891,824]
    # settings (DO NOT TOUCH)
    defaultUpperLeft = [0,295]
    defaultLowerRight = [891,824]
    #print([x, y], [(x-defaultUpperLeft[0])/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0])+upperLeft[0], (y-defaultUpperLeft[1])/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])+upperLeft[1]])
    return (x-defaultUpperLeft[0])/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0])+upperLeft[0], (y-defaultUpperLeft[1])/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])+upperLeft[1]

# Dark Castle eady mode monkey money farm and collection event grinder
# • fully automatic
# • approx 600 MM / hour
# • approx 40 tokens / hour
# • timing based
# • no hero used
# • mk required (increased starting cash, military conscription, probs a few others)
# • automatic error handling (level up, unfocused window)
# • dies to internet and lag
# 
# Start a easy standard game on dark castle, then run script
# it will automatically start game and beat it repeatedly
def darkCastle(): 
    t = 0
    while (1):
        s1 = [680,590] # position of sniper 1 on screen (full auto sniper)
        s2 = [680,550] # position of sniper 2 on screen (deadly precision sniper)
        print('Initialising...')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(400, 500))
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        placeTower(s1, 'q')
        print('Placed sniper1')
        time.sleep(0.25)
        placeTower(s2, 'q')
        print('Placed sniper2')
        time.sleep(0.5)
        upgradeTower(s1, 2)
        print('upgrade sniper1 0 1 0')
        time.sleep(17)
        upgradeTower(s1, 2)
        print('upgrade sniper1 0 2 0')
        time.sleep(22)
        upgradeTower(s1, 3)
        print('upgrade sniper1 0 2 1')
        time.sleep(20)
        upgradeTower(s1, 3)
        print('upgrade sniper1 0 2 2')
        time.sleep(11)
        upgradeTower(s2, 2)
        print('upgrade sniper2 0 1 0')
        time.sleep(20)
        upgradeTower(s2, 2)
        print('upgrade sniper2 0 2 0')
        time.sleep(20)
        upgradeTower(s2, 1)
        print('upgrade sniper2 1 2 0') 
        time.sleep(75)
        upgradeTower(s1, 3)
        print('upgrade sniper2 0 2 3') 
        time.sleep(70)
        upgradeTower(s1, 3)
        print('upgrade sniper2 0 2 4') 
        time.sleep(22)
        upgradeTower(s2, 1)
        print('upgrade sniper2 2 2 0') 
        time.sleep(40)
        upgradeTower(s2, 1)
        print('upgrade sniper2 3 2 0') 
        time.sleep(30)
        t += 1
        print(f'completed {t} games, generated {t*60} total monkey money')
        pyautogui.click(scaleCoords(400, 400)) # handle levelup
        time.sleep(0.1)
        pyautogui.click(scaleCoords(400, 400))
        time.sleep(0.1)
        pyautogui.click(scaleCoords(450, 740))
        time.sleep(0.5)
        pyautogui.click(scaleCoords(330, 720))
        time.sleep(3)
        pyautogui.click(scaleCoords(380, 750))
        time.sleep(1)
        pyautogui.click(scaleCoords(630, 770))
        time.sleep(0.5)
        pyautogui.click(scaleCoords(780, 500))
        time.sleep(0.5)
        pyautogui.click(scaleCoords(250, 600))
        time.sleep(0.5)
        pyautogui.click(scaleCoords(280, 500))
        time.sleep(0.5)
        pyautogui.click(scaleCoords(300, 600))
        time.sleep(5)

# Infernal chimps monkey money farm, collection event grinder and instamonkey farm
# • fully automatic
# • approx 600 MM / hour
# • approx 42 tokens / hour
# • approx 3 instas / hour
# • image recognition based
# • psi hero used
# • mk not used (chimps)
# • automatic error handling (level up, unfocused window)
# • dies to internet
# 
# Start a chimps game on infernal, then run script
# it will automatically start game and beat it repeatedly
# it will automatically close the chimps dialogue box
def infernal():
    while (1): # start new games
        print('starting game')
        pyautogui.click(scaleCoords(400, 400)) # focus
        time.sleep(0.1)
        pyautogui.click(scaleCoords(380, 750)) # play
        time.sleep(0.2)
        pyautogui.click(scaleCoords(40, 380)) # search button
        time.sleep(0.1)
        pyautogui.click(scaleCoords(390, 320)) # search bar
        time.sleep(0.1)
        pyautogui.typewrite('infernal')
        time.sleep(0.1)
        pyautogui.click(scaleCoords(230, 460)) # infernal
        time.sleep(0.1)
        pyautogui.click(scaleCoords(600, 500)) # hard
        time.sleep(0.2)
        pyautogui.click(scaleCoords(760, 660)) # chimps
        time.sleep(5)
        pyautogui.click(scaleCoords(440, 660)) # ok
        time.sleep(0.5)
        psi = [214,417]
        boomer = [385,635]
        alc = [404, 662]
        wiz = [368,663]
        sniper = [732, 585]
        bomb = [42, 618]
        spactory = [396, 482]
        alc2 = [379, 442]
        actions = [
            {'type': 'p', 'key': 'o', 'cost': 350, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 190, 'pos': boomer},
            {'type': 'u', 'key': '3', 'cost': 110, 'pos': boomer},
            {'type': 'start', 'cost': 0},
            {'type': 'u', 'key': '3', 'cost': 325, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': boomer},
            {'type': 'p', 'key': '`', 'cost': 1080, 'pos': psi},
            {'type': 'u', 'key': '3', 'cost': 1405, 'pos': boomer},
            {'type': 'u', 'key': '3', 'cost': 2460, 'pos': boomer},
            {'type': 'p', 'key': 'a', 'cost': 595, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 270, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 380, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 1350, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 3240, 'pos': alc},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': alc},
            {'type': 'u', 'key': '2', 'cost': 515, 'pos': alc},
            {'type': 'p', 'key': 'w', 'cost': 405, 'pos': wiz},
            {'type': 'u', 'key': '1', 'cost': 135, 'pos': wiz},
            {'type': 'u', 'key': '1', 'cost': 485, 'pos': wiz},
            {'type': 'u', 'key': '3', 'cost': 300, 'pos': wiz},
            {'type': 'u', 'key': '3', 'cost': 325, 'pos': wiz},
            {'type': 'u', 'key': '3', 'cost': 1620, 'pos': wiz},
            {'type': 'u', 'key': '3', 'cost': 3025, 'pos': wiz},
            {'type': 'p', 'key': 'b', 'cost': 565, 'pos': bomb},
            {'type': 'u', 'key': '4', 'cost': 0, 'pos': bomb}, # change targeting to strong
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': bomb},
            {'type': 'u', 'key': '2', 'cost': 430, 'pos': bomb},
            {'type': 'u', 'key': '2', 'cost': 1190, 'pos': bomb},
            {'type': 'u', 'key': '3', 'cost': 215, 'pos': bomb},
            {'type': 'u', 'key': '3', 'cost': 28620, 'pos': wiz},
            {'type': 'u', 'key': '3', 'cost': 51300, 'pos': boomer},
            {'type': 'p', 'key': 'x', 'cost': 1080, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 160, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 430, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 1510, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 3780, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 32400, 'pos': spactory},
            {'type': 'u', 'key': '2', 'cost': 650, 'pos': spactory},
            {'type': 'u', 'key': '2', 'cost': 865, 'pos': spactory},
            {'type': 'u', 'key': '4', 'cost': 0, 'pos': spactory}, #change targeting to smart
            {'type': 'p', 'key': 'a', 'cost': 595, 'pos': alc2},
            {'type': 'u', 'key': '1', 'cost': 270, 'pos': alc2},
            {'type': 'u', 'key': '1', 'cost': 380, 'pos': alc2},
            {'type': 'u', 'key': '1', 'cost': 1350, 'pos': alc2},
            {'type': 'u', 'key': '1', 'cost': 3240, 'pos': alc2},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': alc2},
            {'type': 'u', 'key': '2', 'cost': 515, 'pos': alc2},
            ]
        print('Initialising...')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(400, 500))
        time.sleep(0.5)
        while len(actions) > 0: # check if actions can be performed
            pyautogui.click(scaleCoords(400, 400)) # handle levelup
            time.sleep(0.1)
            pyautogui.click(scaleCoords(400, 400))
            time.sleep(0.1)
            #wprint(f'next move: {actions[0]}')
            action = actions[0]
            if (action['type'] == 'u'):
                selectTower(action['pos'])
                print('selected')
                time.sleep(0.25)
                if canUpgrade(int(action['key'])):
                    print('check upgrade')
                    time.sleep(0.1)
                    upgradeTower(action['pos'], int(action['key']))
                    print('upgraded')
                    actions.pop(0)
                time.sleep(0.5)
            else:
                cash = getMoney()
                if cash != '':
                    cash = int(cash)
                else:
                    print('failed to detect money')
                    cash = 0
                if (cash >= action['cost']):
                    if action['type'] == 'p':
                        placeTower(action['pos'], action['key'])
                    elif action['type'] == 'start':
                        pyautogui.press('enter')
                        time.sleep(0.1)
                        pyautogui.press('enter')
                        time.sleep(0.1)
                    actions.pop(0)
                    time.sleep(0.5)
        print('defense done')
        while 1:
            if checkComplete():
                print('reset')
                pyautogui.click(scaleCoords(440, 600)) # collect insta
                time.sleep(2)
                pyautogui.click(scaleCoords(440, 750)) # next
                time.sleep(1)
                pyautogui.click(scaleCoords(325, 700)) # home
                time.sleep(5)
                print('reset complete')
                break
            else:
                time.sleep(1)



        
