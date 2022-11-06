import time
import board
import digitalio
import usb_hid
import json
import io
import neopixel
import initializer

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keyboardext.keyboardext import Keyboardext
from adafruit_hid.consumer_control import ConsumerControl

with open("keys.json") as infile:
    jsonData = json.load(infile)

sleepTime = 60000

pixelsInitializer = initializer.Pixels()
pixels = pixelsInitializer.getPixels()
pixelMap = pixelsInitializer.getPixelMap()
kbd = Keyboardext(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

def main():

    buttons = initializer.Buttons()
    keyButtons = buttons.getButtons()

    buttonsPressed = [True, True, True, True, True, True, True, True, True]
    buttonTimer = [0,0,0,0,0,0,0,0,0]
    buttonRunCounter = [0,0,0,0,0,0,0,0,0]
    lastButtonPressed = now()

    while True:
        try:
            kbd = Keyboardext(usb_hid.devices)
            consumer_control = ConsumerControl(usb_hid.devices)
        except:
            pixels.brightness = 0
            print("Keyboard disconnected")

        if now() - lastButtonPressed > sleepTime:
            pixels.brightness = .1

        for id in keyButtons:
            currentButton = False
            if keyButtons[id].value:
                currentButton = True
                lastButtonPressed = now()
                pixels.brightness = 1
            if buttonsPressed[id] != currentButton:
                buttonsPressed[id] = currentButton

                if currentButton == True:
                    buttonTimer[id] = now()
                    buttonRunCounter[id] = 0
                print("Button #",str(id)," is ",("released", "pressed")[currentButton])

                if currentButton == False:
                    print("pressed for ", now() - buttonTimer[id],"ms")
                buttonAction(id, currentButton)
            if "repeat" in jsonData[id]:
                if now() - buttonTimer[id] - jsonData[id]["repeat"]["after"] - (jsonData[id]["repeat"]["delay"] * buttonRunCounter[id]) > 0:
                    buttonRunCounter[id] += 1
                    buttonAction(id, currentButton)

def buttonAction(id, state):

    if state:
        pixels[pixelMap[id]] = (255, 255, 255)
        if "string" in jsonData[id]:
            kbd.set_layout(jsonData[id]["string"]["layout"])
            kbd.write(jsonData[id]["string"]["keys"])
        if "consumerControl" in jsonData[id]:
            for controlKey in jsonData[id]["consumerControl"]:
                consumer_control.send(controlKey)

        pixels[pixelMap[id]] = (0, 0, 0)
    else:
        pixels[pixelMap[id]] = jsonData[id]["color"]

def now():
    return int(time.monotonic_ns()/1000000)

if __name__ == "__main__":
    main()
