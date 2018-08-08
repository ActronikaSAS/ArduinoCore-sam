# Arduino Core for SAM3X CPU

This repository contains the source code and configuration files of the Arduino Core for Atmel's SAM3X processor (used on the [Arduino Due](https://www.arduino.cc/en/Main/ArduinoBoardDue) board).

## Installation on Arduino IDE

First, uninstall the package named:  
**Arduino SAM Boards (32-bit ARM Cortex-M3)**

Then, run `install.py` with python 3.x and with the settings directory of your arduino IDE as argument.

Usually this directory is located at `/home/username/.arduino15/` so the commandline is:  
>`python3 install.py /home/username/.arduino15/`

Restart Arduino IDE  
The boards **Actronika Arduino ARM (32-bits) Boards** should now appear in the boards menu in your Arduino IDE
