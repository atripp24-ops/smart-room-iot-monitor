from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=5000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.fill(0)
oled.text("Hello Matt", 0, 0)
oled.text("OLED Works", 0, 20)
oled.show()

