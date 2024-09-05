import pyautogui
import time
import math
import copy
import pytesseract
from PIL import Image, ImageOps

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
        self.sub = "u"
        self.dart = 'l'
        self.boat = "c"
        self.ace = "p"

        self.display = { # set your btd6 screen position with 2 corner coordinates 
            # side by side
            # "upperLeft": [0, 295],
            # "lowerRight": [891, 824]

            # full screen
            "upperLeft": [0, 26],
            "lowerRight": [1791, 1093]
        }

data = keybinds()
strats = {
    "bloody": {
        "sub1": [1118, 225],
        "sub2": [548, 679],
        "dart1": [353, 571],
        "boat1": [229, 489],
        "boat2": [1025, 945],
    },
    "ravine": {
        "dart1": [244, 687],
        "dart2": [675, 831],
        "boomer1": [1253, 332],
        "boomer2": [642, 185],
        "boomer3": [748, 976],
        "bomb": [706, 226]
    },
    "dungeon": {
        "sub": [1282, 871],
        "boomer": [211, 821],
        "dart": [595, 540],
        "plane": [975, 655],
        "alc": [975, 585],
    }
}
strats["bloody"]["actions"] = [
    {'type': 'p', 'key': data.sub, 'cost': 170, 'pos': strats["bloody"]["sub1"]},
    {'type': 'p', 'key': data.dart, 'cost': 0, 'pos': strats["bloody"]["dart1"]},
    {'type': 'start', 'cost': 0},
    {'type': 'p', 'key': data.sub, 'cost': 260, 'pos': strats["bloody"]["sub2"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub1']},
    {'type': 'p', 'key': data.boat, 'cost': 325, 'pos': strats["bloody"]["boat1"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]["boat1"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub1']},
    {'type': 'u', 'key': '1', 'pos': strats["bloody"]['sub1']},
    {'type': 'u', 'key': '1', 'pos': strats["bloody"]['sub1']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '1', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '1', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]["boat1"]},
    {'type': 'u', 'key': '2', 'pos': strats["bloody"]["boat1"]},
    {'type': 'u', 'key': '2', 'pos': strats["bloody"]["boat1"]},
    {'type': 'p', 'key': data.boat, 'cost': 325, 'pos': strats["bloody"]["boat2"]},
    {'type': 'u', 'key': '2', 'pos': strats["bloody"]["boat2"]},
    {'type': 'u', 'key': '2', 'pos': strats["bloody"]["boat2"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]["boat2"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]["boat2"]},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub1']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub2']},
    {'type': 'u', 'key': '3', 'pos': strats["bloody"]['sub1']},
]
strats["ravine"]["actions"] = [
    {'type': 'p', 'key': data.dart, 'cost': 0, 'pos': strats["ravine"]["dart1"]},
    {'type': 'p', 'key': data.dart, 'cost': 170, 'pos': strats["ravine"]["dart2"]},
    {'type': 'start', 'cost': 0},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['dart1']},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['dart1']},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['dart2']},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['dart2']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart2']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart1']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart2']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart2']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart1']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart1']},
    {'type': 'p', 'key': data.boomerang, 'cost': 220, 'pos': strats["ravine"]["boomer1"]},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer1']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer1']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer1']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer1']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer1']},
    {'type': 'p', 'key': data.boomerang, 'cost': 220, 'pos': strats["ravine"]["boomer2"]},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer2']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer2']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer2']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer2']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer2']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer1']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['dart2']},
    {'type': 'p', 'key': data.bombShooter, 'cost': 320, 'pos': strats["ravine"]["bomb"]},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['bomb']},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['bomb']},
    {'type': 'u', 'key': '2', 'pos': strats["ravine"]['bomb']},
    {'type': 'p', 'key': data.boomerang, 'cost': 220, 'pos': strats["ravine"]["boomer3"]},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer3']},
    {'type': 'u', 'key': '3', 'pos': strats["ravine"]['boomer3']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer3']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer3']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer3']},
    {'type': 'u', 'key': '1', 'pos': strats["ravine"]['boomer3']},
]
strats["dungeon"]["actions"] = [
    {'type': 'p', 'key': data.dart, 'cost': 0, 'pos': strats["dungeon"]["dart"]},
    {'type': 'p', 'key': data.sub, 'cost': 170, 'pos': strats["dungeon"]["sub"]},
    {'type': 'p', 'key': data.boomerang, 'cost': 220, 'pos': strats["dungeon"]["boomer"]},
    {'type': 'start', 'cost': 0},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['boomer']},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['boomer']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['dart']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['dart']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['boomer']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['boomer']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['dart']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['dart']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['dart']},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['sub']},
    {'type': 'p', 'key': data.ace, 'cost': 645, 'pos': strats["dungeon"]["plane"]},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['plane']},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['plane']},
    {'type': 'u', 'key': '3', 'pos': strats["dungeon"]['plane']},
    {'type': 'p', 'key': data.alchemist, 'cost': 470, 'pos': strats["dungeon"]["alc"]},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['alc']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['alc']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['plane']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['plane']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['alc']},
    {'type': 'u', 'key': '1', 'pos': strats["dungeon"]['alc']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['alc']},
    {'type': 'u', 'key': '2', 'pos': strats["dungeon"]['alc']},
]

def ocr(pos1, pos2):
    upperLeftX, upperLeftY = scaleCoords(pos1)
    x, y = scaleCoords(pos2)
    img = pyautogui.screenshot('image.png', region=(int(upperLeftX), int(upperLeftY), int(x), int(y)))
    time.sleep(0.25)

    # Convert image to grayscale and then apply a threshold to make it black and white
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: p > 240 and 255)  # Thresholding to make the text white

    time.sleep(0.25)
    txt = pytesseract.image_to_string(img)
    print(f'IMAGE RECOGNITION: Found text {txt}')
    return txt.lower()

def scaleCoords(x, y=-1): 
    if isinstance(x, list):
        x, y = x
    # your btd6 display size (change to fit your screen)
    upperLeft = data.display['upperLeft']
    lowerRight = data.display['lowerRight']
    # settings (DO NOT TOUCH)
    defaultUpperLeft = [0, 26]
    defaultLowerRight =  [1791, 1093]
    #print([x, y], [(x-defaultUpperLeft[0])/(defaultLowerRight[0]-defaultUpperLeft[0])*(lowerRight[0]-upperLeft[0])+upperLeft[0], (y-defaultUpperLeft[1])/(defaultLowerRight[1]-defaultUpperLeft[1])*(lowerRight[1]-upperLeft[1])+upperLeft[1]])
    return (x - defaultUpperLeft[0]) * (lowerRight[0] - upperLeft[0]) / (defaultLowerRight[0] - defaultUpperLeft[0]) + upperLeft[0], (y - defaultUpperLeft[1]) * (lowerRight[1] - upperLeft[1]) / (defaultLowerRight[1] - defaultUpperLeft[1]) + upperLeft[1]

def handleLevelUp():
    pyautogui.click(scaleCoords(1670, 1080)) # focus
    time.sleep(0.25)
    pyautogui.click(scaleCoords(1670, 1080)) # focus
    time.sleep(0.25)

def upgradeTower(path):
    if path == '1':
        key = data.upgradePath1
    elif path == '2':
        key = data.upgradePath2
    elif path == '3':
        key = data.upgradePath3
    elif path == '4':
        key = data.changeTargeting
    elif path == '5':
        key = data.reverseChangeTargeting
    pyautogui.typewrite(key)

def canUpgrade(path): # no paragon support
    p1XL, p1YL = scaleCoords(235,508)
    p2XL, p2YL = scaleCoords(235,654)
    p3XL, p3YL = scaleCoords(235,800)
    p1XR, p1YR = scaleCoords(1384,508)
    p2XR, p2YR = scaleCoords(1384,654)
    p3XR, p3YR = scaleCoords(1384,800)
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

def game(actions):
    while len(actions) > 0: # check if actions can be performed
        handleLevelUp()
        action = actions[0]
        if (action['type'] == 'u'): # upgrade
            pyautogui.click(scaleCoords(action['pos']))
            time.sleep(0.25)
            print('selected')
            if canUpgrade(int(action['key'])):
                upgradeTower(action['key'])
                print('upgraded')
                actions.pop(0)
                pyautogui.press('esc')
        else: 
            if action['type'] == 'start': # start game
                pyautogui.press('enter')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(0.1)
                actions.pop(0)
                time.sleep(0.5)
            else: # place towers
                # get money
                raw = ocr([335, 60], [450, 100])
                cash = ''
                for char in raw:
                    if char.isnumeric():
                        cash += char
                if cash != '':
                    cash = int(cash)
                else:
                    print('failed to detect money')
                    cash = 0

                if (cash >= action['cost']):
                    if action['type'] == 'p':
                        pyautogui.typewrite(action['key'])
                        pyautogui.click(scaleCoords(action['pos']))
                        actions.pop(0)
                        time.sleep(0.5)

# Expert Easy collection event grinder
# • full automatic
# • 
# • 
# • no hero used
# • mk used
# • automatic error handling (level up, unfocused window)
# • dies to internet if there is collection event
# • idk if there is rng, probably none
# 
# run script on home page
# it will automatically start games and beat it repeatedly
def grindCollectionEvent():
    time.sleep(1)
    while (1): # start new games
        print('starting game')
        pyautogui.click(scaleCoords(200, 200)) # focus (anywhere on scrren that is not a button)
        time.sleep(0.2)
        pyautogui.click(scaleCoords(780, 950)) # play
        time.sleep(0.75)
        pyautogui.click(scaleCoords(75, 190)) # search button
        time.sleep(0.25)
        pyautogui.click(scaleCoords(740, 70)) # search bar
        time.sleep(0.25)
        pyautogui.typewrite('/CollectionEvent')
        time.sleep(0.5)

        while (1):
            map = ocr([300, 525], [650, 570])
            print(map)

            if "bloody" in map:
                print('Playing Bloody Puddles')
                actions = copy.deepcopy(strats["bloody"]["actions"])
                break
            elif 'ravine' in map:
                print('Playing Ravine')
                actions = copy.deepcopy(strats["ravine"]["actions"])
                break
            elif 'dark' in map:
                print('Playing Dark Dungeons')
                actions = copy.deepcopy(strats["dungeon"]["actions"])
                break
            
            print('map not found, trying again')
        
        pyautogui.click(scaleCoords(480, 660)) # expert
        time.sleep(0.75)
        pyautogui.click(scaleCoords(570, 600)) # easy
        time.sleep(0.75)
        pyautogui.click(scaleCoords(580, 620)) # standard
        time.sleep(6)
        
        print('Initialising...')
        pyautogui.click(scaleCoords(1670, 1080)) # focus
        time.sleep(0.5)
        
        game(actions) # play the game
                
        print('done')
        while 1:
            handleLevelUp()
            raw = ocr([540, 280], [1200, 900])
            if 'insta' in raw.lower():
                print('reset')
                pyautogui.click(scaleCoords(900, 600)) # victory screen (dispel insta monkey notification if any)
                time.sleep(2)
                pyautogui.click(scaleCoords(900, 925)) # next
                time.sleep(1)
                pyautogui.click(scaleCoords(650, 870)) # home
                time.sleep(5)
                print('reset complete')
                break

print('ready...')
time.sleep(2)
#game(strats["dungeon"]["actions"])
grindCollectionEvent()