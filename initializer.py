
import digitalio
import board
import neopixel

class Buttons:

    keyButtons = {}

    def __init__(self):
        self.keyButtons[0] = digitalio.DigitalInOut(board.GP7)
        self.keyButtons[1] = digitalio.DigitalInOut(board.GP8)
        self.keyButtons[2] = digitalio.DigitalInOut(board.GP9)
        self.keyButtons[3] = digitalio.DigitalInOut(board.GP4)
        self.keyButtons[4] = digitalio.DigitalInOut(board.GP5)
        self.keyButtons[5] = digitalio.DigitalInOut(board.GP6)
        self.keyButtons[6] = digitalio.DigitalInOut(board.GP1)
        self.keyButtons[7] = digitalio.DigitalInOut(board.GP2)
        self.keyButtons[8] = digitalio.DigitalInOut(board.GP3)

        for id in self.keyButtons:
            self.keyButtons[id].direction = digitalio.Direction.INPUT
            self.keyButtons[id].pull = digitalio.Pull.DOWN

    def getButtons(self):
        return self.keyButtons

class Pixels:

    pixels = {}

    def __init__(self):

        self.pixels = neopixel.NeoPixel(board.GP28, 9)
        self.pixels.brightness = 1

    def getPixels(self):
        return self.pixels

    def getPixelMap(self):
        pixelMap = {}
        pixelMap[0] = 0
        pixelMap[1] = 3
        pixelMap[2] = 6
        pixelMap[3] = 1
        pixelMap[4] = 4
        pixelMap[5] = 7
        pixelMap[6] = 2
        pixelMap[7] = 5
        pixelMap[8] = 8
        return pixelMap
