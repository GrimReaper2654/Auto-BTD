import pyautogui
import time, math
#from playsound import playsound

# use pytesseract for text recognition (requires download)
from PIL import Image
import pytesseract
# update according to your installation
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

class keybinds(): # change based on your own keybinds
    def __init__(self):
        self.upgradePath1 = ','
        self.upgradePath2 = '.'
        self.upgradePath3 = '/'
        self.changeTargeting = ']'
        self.reverseChangeTargeting = '\\'
        self.hero = '`'
        self.sniper = 'q'
        self.boomerang = 'o'
        self.alchemist = 'a'
        self.spikeFactory = 'x'
        self.bombShooter = 'b'
        self.mermonkey = 'm'

        self.display = { # set your btd6 screen position with 2 corner coordinates 
            "upperLeft": [0,295],
            "lowerRight": [891,824]
        }

data = keybinds()

def placeTower(pos, key):
    pyautogui.typewrite(key)
    time.sleep(0.1)
    pyautogui.click(scaleCoords(pos[0], pos[1]))
    time.sleep(0.1)

def handleLevelUp():
    pyautogui.click(scaleCoords(860, 816)) # handle levelup
    time.sleep(0.25)
    pyautogui.click(scaleCoords(860, 816)) # click just below play button
    time.sleep(0.25)

def selectTower(pos):
    pyautogui.click(scaleCoords(pos[0], pos[1]))
    time.sleep(0.1)

def upgradeTower(pos, path): # I can't be bothered removing the unnecessary parameter
    if path == 1:
        key = data.upgradePath1
    elif path == 2:
        key = data.upgradePath2
    elif path == 3:
        key = data.upgradePath3
    elif path == 4:
        key = data.changeTargeting
    elif path == 5:
        key = data.reverseChangeTargeting
    pyautogui.typewrite(key)

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
    X, Y = scaleCoords(180,45, False)
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
        L = pyautogui.screenshot(region=(int(p1XL), int(p1YL), 1, 1))
        R = pyautogui.screenshot(region=(int(p1XR), int(p1YR), 1, 1))
        time.sleep(0.2)
        print(L.getcolors())
        print(R.getcolors())
        if (abs(L.getcolors()[0][1][0] - 127) < 10 and abs(L.getcolors()[0][1][1] - 219) < 10 and abs(L.getcolors()[0][1][2] - 66) < 10) or (abs(R.getcolors()[0][1][0] - 127) < 10 and abs(R.getcolors()[0][1][1] - 219) < 10 and abs(R.getcolors()[0][1][2] - 66) < 10):
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    elif path == 2:
        #[(4, (127, 219, 66, 255))]
        L = pyautogui.screenshot(region=(int(p2XL), int(p2YL), 1, 1))
        R = pyautogui.screenshot(region=(int(p2XR), int(p2YR), 1, 1))
        time.sleep(0.2)
        print(L.getcolors())
        print(R.getcolors())
        if (abs(L.getcolors()[0][1][0] - 127) < 10 and abs(L.getcolors()[0][1][1] - 219) < 10 and abs(L.getcolors()[0][1][2] - 66) < 10) or (abs(R.getcolors()[0][1][0] - 127) < 10 and abs(R.getcolors()[0][1][1] - 219) < 10 and abs(R.getcolors()[0][1][2] - 66) < 10):
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    elif path == 3:
        L = pyautogui.screenshot(region=(int(p3XL), int(p3YL), 1, 1))
        R = pyautogui.screenshot(region=(int(p3XR), int(p3YR), 1, 1))
        time.sleep(0.2)
        print(L.getcolors())
        print(R.getcolors())
        if (abs(L.getcolors()[0][1][0] - 127) < 10 and abs(L.getcolors()[0][1][1] - 219) < 10 and abs(L.getcolors()[0][1][2] - 66) < 10) or (abs(R.getcolors()[0][1][0] - 127) < 10 and abs(R.getcolors()[0][1][1] - 219) < 10 and abs(R.getcolors()[0][1][2] - 66) < 10):
            print('can upgrade')
            return True
        print('cant upgrade')
        return False
    else:
        print('change targeting detected')
        return True

def checkComplete():
    upperLeftX, upperLeftY = scaleCoords(355,610)
    X, Y = scaleCoords(180,60, False)
    img = pyautogui.screenshot('complete.png', region=(int(upperLeftX), int(upperLeftY), int(X), int(Y)))
    time.sleep(0.5)
    txt = pytesseract.image_to_string(img)
    print(f'IMAGE RECOGNITION: {txt}')
    if 'insta' in txt.lower():
        return True
    return False

def scaleCoords(x, y, scuffed = True): 
    # your btd6 display size (change to fit your screen)
    upperLeft = data.display['upperLeft']
    lowerRight = data.display['lowerRight']
    # settings (DO NOT TOUCH)
    defaultUpperLeft = [0,295]
    defaultLowerRight = [891,824]
    #print([x, y], [(x-defaultUpperLeft[0])/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0])+upperLeft[0], (y-defaultUpperLeft[1])/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])+upperLeft[1]])
    if scuffed:
        return (x-defaultUpperLeft[0])/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0])+upperLeft[0], (y-defaultUpperLeft[1])/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])+upperLeft[1]
    return x/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0]), y/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])

# Dark Castle eady mode monkey money farm and collection event grinder
# • fully automatic
# • approx 600 MM / hour
# • approx 40 tokens / hour
# • no hero used
# • mk required (increased starting cash, military conscription, probs a few others)
# • automatic error handling (level up, unfocused window)
# • dies to internet if there is collection event
# • no rng at all
# 
# run script on home page
# it will automatically start game and beat it repeatedly
def darkCastleEasy(): 
    time.sleep(1)
    while (1): # start new games
        print('starting game')
        pyautogui.click(scaleCoords(400, 400)) # focus
        time.sleep(0.2)
        pyautogui.click(scaleCoords(380, 750)) # play
        time.sleep(0.5)
        pyautogui.click(scaleCoords(40, 380)) # search button
        time.sleep(0.5)
        pyautogui.click(scaleCoords(390, 320)) # search bar
        time.sleep(0.5)
        pyautogui.typewrite('dark castle')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(230, 460)) # dark castle
        time.sleep(0.5)
        pyautogui.click(scaleCoords(270, 500)) # easy
        time.sleep(0.5)
        pyautogui.click(scaleCoords(300, 580)) # standard
        time.sleep(5)
        s1 = [680,590] # position of sniper 1 on screen (full auto sniper)
        s2 = [680,550] # position of sniper 2 on screen (maim moab sniper)
        actions = [
            {'type': 'start', 'cost': 0},
            {'type': 'p', 'key': data.sniper, 'cost': 0, 'pos': s1},
            {'type': 'p', 'key': data.sniper, 'cost': 0, 'pos': s2},
            {'type': 'u', 'key': '2', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '2', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '2', 'cost': -1, 'pos': s2},
            {'type': 'u', 'key': '2', 'cost': -1, 'pos': s2},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': s2},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': s1},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': s2},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': s2},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': s2},
        ]
        print('Initialising...')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(400, 500))
        time.sleep(0.5)
        notSelected = True
        while len(actions) > 0: # check if actions can be performed
            #print(f'next move: {actions[0]}')
            handleLevelUp()
            action = actions[0]
            if (action['type'] == 'u'):
                if notSelected:
                    selectTower(action['pos'])
                    notSelected = False
                    print('selected')
                    time.sleep(0.25)
                if canUpgrade(int(action['key'])):
                    #time.sleep(0.1)
                    upgradeTower(action['pos'], int(action['key']))
                    print('upgraded')
                    actions.pop(0)
                    pyautogui.press('esc')
                    notSelected = True
                #time.sleep(0.25)
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
            handleLevelUp()
            if checkComplete():
                print('reset')
                pyautogui.click(scaleCoords(440, 750)) # next
                time.sleep(1)
                pyautogui.click(scaleCoords(325, 700)) # home
                time.sleep(5)
                print('reset complete')
                break
            else:
                time.sleep(1)

# Infernal chimps monkey money farm, collection event grinder and instamonkey farm
# • semi automatic
# • approx 600 MM / hour
# • approx 42 tokens / hour
# • approx 3 instas / hour
# • psi hero used
# • mk not used (chimps)
# • automatic error handling (level up, unfocused window)
# • dies to internet if there is collection event
# • slight rng causes death occasionally (can't run overnight)
# 
# run script on home page
# it will automatically start game and beat it repeatedly
# it will automatically close the chimps dialogue box
def infernalChimps():
    time.sleep(1)
    while (1): # start new games
        print('starting game')
        pyautogui.click(scaleCoords(400, 400)) # focus
        time.sleep(0.2)
        pyautogui.click(scaleCoords(380, 750)) # play
        time.sleep(0.5)
        pyautogui.click(scaleCoords(40, 380)) # search button
        time.sleep(0.5)
        pyautogui.click(scaleCoords(390, 320)) # search bar
        time.sleep(0.5)
        pyautogui.typewrite('infernal')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(230, 460)) # infernal
        time.sleep(0.5)
        pyautogui.click(scaleCoords(600, 500)) # hard
        time.sleep(0.5)
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
            {'type': 'p', 'key': data.boomerang, 'cost': 350, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 190, 'pos': boomer},
            {'type': 'u', 'key': '3', 'cost': 110, 'pos': boomer},
            {'type': 'start', 'cost': 0},
            {'type': 'u', 'key': '3', 'cost': 325, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': boomer},
            {'type': 'p', 'key': data.hero, 'cost': 1080, 'pos': psi},
            {'type': 'u', 'key': '3', 'cost': 1405, 'pos': boomer},
            {'type': 'u', 'key': '3', 'cost': 2460, 'pos': boomer},
            {'type': 'p', 'key': data.alchemist, 'cost': 595, 'pos': alc},
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
            #{'type': 'p', 'key': data.bombShooter, 'cost': 565, 'pos': bomb},
            #{'type': 'u', 'key': '4', 'cost': 0, 'pos': bomb}, # change targeting to strong
            #{'type': 'u', 'key': '2', 'cost': 270, 'pos': bomb},
            #{'type': 'u', 'key': '2', 'cost': 430, 'pos': bomb},
            #{'type': 'u', 'key': '2', 'cost': 1190, 'pos': bomb},
            #{'type': 'u', 'key': '3', 'cost': 215, 'pos': bomb},
            {'type': 'p', 'key': data.sniper, 'cost': 400, 'pos': sniper},
            #{'type': 'u', 'key': '4', 'cost': 0, 'pos': sniper}, # change targeting to strong
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '3', 'cost': 28620, 'pos': wiz},
            {'type': 'u', 'key': '1', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '3', 'cost': -1, 'pos': sniper},
            {'type': 'u', 'key': '3', 'cost': 51300, 'pos': boomer},
            {'type': 'p', 'key': data.spikeFactory, 'cost': 1080, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 160, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 430, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 1510, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 3780, 'pos': spactory},
            {'type': 'u', 'key': '3', 'cost': 32400, 'pos': spactory},
            {'type': 'u', 'key': '2', 'cost': 650, 'pos': spactory},
            {'type': 'u', 'key': '2', 'cost': 865, 'pos': spactory},
            {'type': 'u', 'key': '4', 'cost': 0, 'pos': spactory}, #change targeting to smart
            {'type': 'p', 'key': data.alchemist, 'cost': 595, 'pos': alc2},
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
        notSelected = True
        while len(actions) > 0: # check if actions can be performed
            #print(f'next move: {actions[0]}')
            handleLevelUp()
            action = actions[0]
            if (action['type'] == 'u'):
                if notSelected:
                    selectTower(action['pos'])
                    notSelected = False
                    print('selected')
                    time.sleep(0.25)
                if canUpgrade(int(action['key'])):
                    #time.sleep(0.1)
                    upgradeTower(action['pos'], int(action['key']))
                    print('upgraded')
                    actions.pop(0)
                    pyautogui.press('esc')
                    notSelected = True
                #time.sleep(0.25)
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
            handleLevelUp()
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

# Infernal easy monkey money farm, collection event grinder
# • full automatic
# • approx 600 MM / hour
# • approx 40 tokens / hour
# • psi hero used
# • mk used
# • automatic error handling (level up, unfocused window)
# • dies to internet if there is collection event
# • idk if there is rng, probably none
# 
# run script on home page
# it will automatically start game and beat it repeatedly
def infernalEasy():
    time.sleep(1)
    while (1): # start new games
        print('starting game')
        pyautogui.click(scaleCoords(400, 400)) # focus
        time.sleep(0.2)
        pyautogui.click(scaleCoords(380, 750)) # play
        time.sleep(0.5)
        pyautogui.click(scaleCoords(40, 380)) # search button
        time.sleep(0.5)
        pyautogui.click(scaleCoords(390, 320)) # search bar
        time.sleep(0.5)
        pyautogui.typewrite('infernal')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(230, 460)) # infernal
        time.sleep(0.5)
        pyautogui.click(scaleCoords(270, 500)) # easy
        time.sleep(0.5)
        pyautogui.click(scaleCoords(300, 580)) # standard
        time.sleep(5)
        psi = [214,417]
        boomer = [385,635]
        alc = [404, 662]
        actions = [
            {'type': 'p', 'key': data.boomerang, 'cost': 225, 'pos': boomer},
            {'type': 'start', 'cost': 0},
            {'type': 'u', 'key': '3', 'cost': 110, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 190, 'pos': boomer},
            {'type': 'u', 'key': '3', 'cost': 325, 'pos': boomer},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': boomer},
            {'type': 'p', 'key': data.hero, 'cost': 765, 'pos': psi},
            {'type': 'u', 'key': '3', 'cost': 1405, 'pos': boomer},
            {'type': 'p', 'key': data.alchemist, 'cost': 470, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 270, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 380, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 1350, 'pos': alc},
            {'type': 'u', 'key': '1', 'cost': 3240, 'pos': alc},
            {'type': 'u', 'key': '2', 'cost': 270, 'pos': alc},
            {'type': 'u', 'key': '2', 'cost': 515, 'pos': alc},
            {'type': 'u', 'key': '3', 'cost': 2460, 'pos': boomer},
        ]
        print('Initialising...')
        time.sleep(0.5)
        pyautogui.click(scaleCoords(400, 500))
        time.sleep(0.5)
        notSelected = True
        while len(actions) > 0: # check if actions can be performed
            #print(f'next move: {actions[0]}')
            handleLevelUp()
            action = actions[0]
            if (action['type'] == 'u'):
                if notSelected:
                    selectTower(action['pos'])
                    notSelected = False
                    print('selected')
                    time.sleep(0.25)
                if canUpgrade(int(action['key'])):
                    #time.sleep(0.1)
                    upgradeTower(action['pos'], int(action['key']))
                    print('upgraded')
                    actions.pop(0)
                    pyautogui.press('esc')
                    notSelected = True
                #time.sleep(0.25)
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
            handleLevelUp()
            if checkComplete():
                print('reset')
                pyautogui.click(scaleCoords(440, 600)) # victory screen
                time.sleep(2)
                pyautogui.click(scaleCoords(440, 750)) # next
                time.sleep(1)
                pyautogui.click(scaleCoords(325, 700)) # home
                time.sleep(5)
                print('reset complete')
                break
            else:
                time.sleep(1)

darkCastleEasy()

