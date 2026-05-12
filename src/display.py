#display

from machine import Pin, I2C
import ssd1306

# Create I2C connection
i2c = I2C(0, scl=Pin(17), sda = Pin(16))

# Create OLED object
oled = ssd1306.SSID1306_I2C(128, 64, i2c)

def update_display(data):
    
    oled.fill(0)
    
    oled.text("Smart Room", 0, 0)
    oled.text(f"Temp: {data['temp']}F", 0, 20)
    oled.text(f"Hum: {data['humidity']}%", 0, 35)
    
    if data["motion"]:
        oled.text("Occupied", 0, 50)
    else:
        oled.text("Empty", 0, 50)
        
    oled.show()