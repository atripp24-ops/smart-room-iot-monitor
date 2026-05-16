# Smart Room IoT Monitor

## Project Overview

This project is a Smart Room IoT Monitor built using a Raspberry Pi Pico W and MicroPython.

The system monitors:

* Temperature
* Humidity
* Room occupancy/motion

The Pico W connects to WiFi and hosts a local website that displays the sensor data.

---

# Hardware Used

* Raspberry Pi Pico W
* DHT11 Temperature/Humidity Sensor
* PIR Motion Sensor
* Breadboard
* Jumper Wires

---

# Features

* WiFi connection
* Local web server
* Temperature monitoring
* Humidity monitoring
* Motion detection
* Browser-based dashboard
* MQTT support

---

# Files

| File           | Purpose            |
| -------------- | ------------------ |
| main.py        | Main program loop  |
| do_connect.py  | WiFi connection    |
| sensors.py     | Sensor readings    |
| web_server.py  | Website/server     |
| mqtt_client.py | MQTT communication |
| secrets.py     | WiFi settings      |

---

# How It Works

1. The Pico W connects to WiFi.
2. Sensor data is collected.
3. The Pico hosts a local webpage.
4. A browser can connect to the Pico IP address.
5. The webpage displays room data.

Example:

[http://192.168.x.x](http://192.168.x.x)

---

# Technical Elements Used

* Digital sensors (DHT11 and PIR)
* Networking (HTTP web server)
* MQTT publish/subscribe
* Embedded programming with MicroPython

---

# Challenges

* Sensor wiring issues
* OLED troubleshooting
* Web server debugging
* Hardware connection stability

---

# What I Learned

* How embedded networking works
* How sensors communicate with microcontrollers
* How web servers operate on embedded devices
* How to debug hardware and software together
* Importance of modular programming

---

# Author

Alex Tripp
ECE 296 Final Project
