import time
import sys
import json
import urllib
from urllib import urequest
from machine import Pin, I2C
import ssd1306
from time import sleep

#schermo
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
# download raw json object
    url = "https://dogechain.info/api/v1/address/balance/DC6Xik1BJzC9XhzgqGVXVDrFGu6WcDgrtH"
    data = urllib.urequest.urlopen(url).read().decode()

# parse json object
    obj = json.loads(data)
    print("Debug:")
    print("balance:" + obj["balance"])
#tutti i cazzi del display:
    balance = obj["balance"]
    title = "Dogecoin"
    by = "By EpicMario71"
    text = "Balance:"

    oled.text(title, 40, 0)
    oled.text(text, 40, 21)
    oled.text(balance, 13,35)
    oled.text(by, 10,53)
    oled.show()
    sleep(10)
# Setup