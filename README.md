# Programming Connected Devices Final Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- Author :[Tareq Md Rabiul Hossain CHY](https://www.linkedin.com/in/tareqmdrabiulhossainchy/), [Nushrat JAHAN](https://www.linkedin.com/in/nushrat-jahan-3275a9178/)
- Final Project for [M.Sc. CPS2 Programming Connected Devices course](https://ci.mines-stetienne.fr/cps2/course/pcd/)
- Based on [Maxime Lefrançois's course](https://ci.mines-stetienne.fr/cps2/course/pcd/#_outline_of_the_lectures)

#GROUP_8

# Project Description
This project's main idea is to control Adafruit FeatherWing 128x32 OLED  display using by mobile BLE application and nRF52840. After successful connection and successful run when the connection between nrf52 and esp32 establishes the led will be enlightened as a mark that ESP32 and nRF52840 are connected. To test the project we need to install a mobile app "Bluefruit connect"([more information](https://learn.adafruit.com/bluefruit-le-connect)).For the app we need to turn on location and bluetooth of our smartphone. Also we need to turn on our hotspot to see time. After that we need to open the "Bluefruit Connect Application". It will show the CIRCUITPY5acc to connect. After connection, we need to go to controller option. There we will have 4 active buttons 1,2,3 and 4 (though there are 8 buttons, we used 1,2,3,4 buttons for out project). For button press 1, a monster will be shown. More button press on button 1 will move the monster to the right by one step. For button press 2, the monster will move left by one step. For button press 3, the monster will switch into another monster. For button press 4, the date time will be shown periodically like stopwatch. Again button press will show static value. Here we are sending signal to nrf52 and nrf52 sends this signal to ESP32. ESP32 displays actions on the OLED. That's how our project works!

# Project files
We implemented out code on code.py(CircuitPython) and boot.py(MicroPython) files. The file boot.py is for esp32 and another file code.py is for nrf52. For implementation we used aioble library, ssd1306.py. For ble connection we used "Bluefruit connect" app. To show date time we used out hostpot name and password. If anyone wants to run the code he or she needs to change the hotspot name and password in the do_connect() function where first parameter is hostpotname and second parameter is password:
```
def do_connect():
 # code above
 wlan.connect('Nushrat', 'idontcare')
 # code below
```

# Components Used
- 1 nrf52840
- 1 esp32
- 1 oled 128x32
- 1 led
- 1 resistor 220 Ω
- 6 wires
- 2 usb cables
- breadboard

We used Visual studio code to run files. Used micropython and circuitpython.

# Mobile Application Connection
 - Enable Bluetooth
 - Enable Location Services
 - Use Bluefruit Connect app
 - Open hotspot of mobile phone

#### Scan for Devices
<img src="img/Bluefruit_Connect 1.jpeg" lt="drawing" width="200" height="400">

#### Connect
<img src="img/Bluefruit_Connect 2.jpeg" lt="drawing" width="200" height="400">

#### Controller
<img src="img/Bluefruit_Connect 3.jpeg" lt="drawing" width="200" height="400">

#### Control Pad
<img src="img/Bluefruit_Connect 4.jpeg" lt="drawing" width="200" height="400">

# Circuit Diagram 

#### Circuit Diagram 1
<img src="img/Circuiit Diagram1.jpeg" lt="drawing" width="400" height="400">

#### Circuit Diagram 2
<img src="img/Circuiit Diagram2.jpeg" lt="drawing" width="400" height="400">

#### Monster Output
<img src="img/Circuiit DiagramOutput.jpeg" lt="drawing" width="400" height="400">

#### Monster Change output
<img src="img/Circuiit DiagramOutput2.jpeg" lt="drawing" width="400" height="400">


# Porject Video

[Whole project's video link](https://drive.google.com/drive/u/2/folders/1haNnrMwmfwNZDpgwAixouyjpcdWlav5K) 

# References

- [Aioble](https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble)
- [Monster](https://github.com/TareqChy1/ESP32_Project)
- [Bluefruit-LE-Connect](https://learn.adafruit.com/bluefruit-le-connect)
- [Using a SSD1306 OLED display](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html?highlight=ssd1306)
- [sources of the `ssd1306.py` MicroPython module](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/ssd1306/ssd1306.py)
- [Adafruit FeatherWing 128x32 OLED display](https://learn.adafruit.com/adafruit-oled-featherwing/)
- [MicroPython quick reference guide on Timers](https://docs.micropython.org/en/latest/esp32/quickref.html#timers)
- [Adafruit Feather Bluefruit Sense]()
- [nRF52840]()