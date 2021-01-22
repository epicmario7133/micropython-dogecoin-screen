# micropython-dogecoin-screen
Dogecoin balance viewer on NodeMCU whit 0.96 i2c screen

Before starting, connect your nodemcu to the internet as shown in this [guide](https://medium.com/@JockDaRock/micropython-esp8266-quick-start-part-4-connect-to-wifi-router-7329076ee330#:~:text=Make%20sure%20your%20ESP8266%20is,to%20your%20ESP8266%20WiFi%20AP.)

then do these commands:

import upip

upip.install("micropython-urllib.urequest") 

Next upload ssd1306.py and dogecoin_screen.py to nodemcu whit thonny

Then connect the NodeMCU to the screen

![alt text](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/05/ESP32_OLED.png "Like dis")

Now change your dogecoin address from dis https://dogechain.info/api/v1/address/balance/DC6Xik1BJzC9XhzgqGVXVDrFGu6WcDgrtH to dis https://dogechain.info/api/v1/address/balance/your_dogecoin_address

now start the program

Do donation whit doge:

DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx

![DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx](https://user-images.githubusercontent.com/56398081/83665414-b01f3200-a5cb-11ea-8a15-4a424647f937.png)
