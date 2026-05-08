# Import the socket library.
# Sockets allow the Pico W to send and receive network data.
import socket

# Define a class named WebServer
class WebServer:
    
    # __init__ runs automatically when you create a WebServer object.
    # ip is the Pico W's IP address from WiFi.
    def __init__(self, ip):
        # Create a variable that belongs to this object
        # It tracks how many times the webpage has been requested
        self.ip = ip
        self.request_count = 0
        
        # Convert the IP address and port 80 into a socket address.
        # Port 80 standard port for normal HTTP websites.
        addr = socket.getaddrinfo(ip, 80)[0][-1]
        # Create a socket object.
        # This is like opening a network endpoint for communication.
        self.socket = socket.socket()
        # Bind the socket to the Pico's IP address and port 80.
        # This tells the Pico: "Listen for web requests at this address."
        self.socket.bind(addr)
        # Start listening for incoming browser connections.
        # The 1 means it allows one waiting connection at a time.
        self.socket.listen(1)
        # Set a short timeout so the program does not get stuck waiting forever.
        # This is important because your main loop still needs to read sensors/MQTT.
        self.socket.settimeout(0.1)
        
        print("Web server running at http://", ip)
    
    # Method that generates the HTML webpage
    def generate_page(self, data):
        # If motion is True, show "Occupied".
        # If motion is False, show "Empty".
        motion = "Occupied" if data["motion"] else "Empty"
    
        # Return the HTTP response and HTML webpage as one big string.
        return f"""HTTP/1.1 200 OK
        <!DOCTYPE html>
        <html>
        <head><title>Smart Room Monitor</title></head>
        <body>
        <h1>Smart Room IoT Monitor</h1>
        <p><b>Status:</b> {motion}</p>
        <p><b>Temp:</b> {data["temp"]} F</p>
        <p><b>Humidity:</b> {data["humidity"]}%</p>
        <p><b>Requests:</b> {self.request_count}</p>
        </body>
        </html>
        """
    
    # This function checks whether a browser/client is trying to connect.
    # If someone opens the Pico's IP address, this function responds with the webpage.
    def check_client(self, data):
        
        # Try to accept a browser connection.
        # If nobody connects, the timeout will cause an OSError.
        try:
            
            # Wait for a client/browser to connect.
            # client is the connection to the browser.
            # addr is the browser/client address.
            client, addr = self.socket.accept()
            
            # Receive the browser's HTTP request.
            # 1024 means read up to 1024 bytes.
            request = client.recv(1024)
            
            # Increase request counter by 1 each time someone loads the page.
            self.request_count += 1
            
            # Create the webpage using the latest sensor data.
            response = self.generate_page(data)
            
            # Send the webpage back to the browser.
            client.send(response)
            
             # Close the connection after sending the page.
            client.close()
            
             # If no browser connects during the timeout, ignore it and continue.
        except OSError:
            pass
    