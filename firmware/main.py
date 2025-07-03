import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import busio
import digitalio
import neopixel
import pwmio

displayio.release_displays()
i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
main_group = displayio.Group()

buzzer = pwmio.PWMOut(board.GP3, duty_cycle=0, frequency=440, variable_frequency=True)


sw_ccw = digitalio.DigitalInOut(board.GP0)
sw_ccw.direction = digitalio.Direction.INPUT
sw_ccw.pull = digitalio.Pull.UP 

sw_cw = digitalio.DigitalInOut(board.GP2)
sw_cw.direction = digitalio.Direction.INPUT
sw_cw.pull = digitalio.Pull.UP

sw_push = digitalio.DigitalInOut(board.GP1)
sw_push.direction = digitalio.Direction.INPUT
sw_push.pull = digitalio.Pull.UP

strip = neopixel.NeoPixel(board.GP6, 1, brightness=0.2, auto_write=True) # INCREASE THIS LATER!!!
strip[0] = (0, 0, 0) 

bpm = 120
last_beat = time.monotonic()
bpm_text = label.Label(terminalio.FONT, text=f"{bpm}", scale=2, x=0, y=16)
main_group.append(bpm_text)

now = 0


def beat():
    global strip, buzzer
    strip[0] = (255, 255, 255)
    buzzer.frequency = 1950
    buzzer.duty_cycle = 32768 # INCREASE THIS LATER!!!


while True:
    now = time.monotonic()
    if sw_ccw.value is False:
        bpm -= 1
        bpm = max(1, bpm)
    elif sw_cw.value is False:
        bpm += 1
        bpm = min(300, bpm)
    elif sw_push.value is False:
        bpm = 0 # this button can be changed later but for now it turns off the metronome
    # we could add debounce here but i'm a minecraft player and we don't do that here

    if bpm > 0 and now % (60 / bpm) <= 0.01:
        beat()
        last_beat = now
    if (now - last_beat) >= 0.05:
        strip[0] = (0, 0, 0)
        buzzer.duty_cycle = 0

    bpm_text.text = f"{bpm}"