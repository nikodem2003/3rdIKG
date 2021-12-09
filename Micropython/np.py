#import rp2
#from neopixel import Neopixel
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(4), 1)

def run():
    np[0] = (0, 0, 0)
    np.write()