#connect

import network
import time

def do_connect (ssid, password):
    # Create a WiFi object in "station mode"
    # (station mode = connect to an existing WiFi network, like your home WiFi)
    wlan = network.WLAN(network.STA_IF)
    
    #Turn on the WiFi hardware on the Pico W 
    wlan.active(True)
    
    # Check if the Pico is NOT already connected to WiFi
    if not wlan.isconnected:
        print("Connecting to Network...")
        # Attempt to connect using SSID and password
        wlan.connect(ssid,password)
        
        # Set a timeout counter (15 seconds max wait)
        timeout = 15
        
         # Keep trying while:
         # 1. Not connected yet
         # 2. Still have time left
        while not wlan.isconnected() and timeout > 0:
            print("Waiting...")
            
            # Wait 1 second before checking again
            time.sleep(1)
            
            # Decrease timeout by 1 each loop (counts down)
            timeout -= 1
    
    # After trying, check if connection was successful
    if wlan.isconnected:
        
        # Print full network info (IP, subnet, gateway, DNS)
        print("Connected" , wlan.ifconfig())
        # Return ONLY the IP address (first item in tuple)
        return wlan.ifconfig()[0]
    else:
        print("Failed to connect")
        # Return None to indicate failure
        return none