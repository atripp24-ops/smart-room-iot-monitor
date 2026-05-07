#web_server

# Define a class named WebServer
class WebServer:
    
    # Constructor method (runs when you create the object)
    def __init__(self):
        # Create a variable that belongs to this object
        # It tracks how many times the webpage has been requested
        self.request_count = 0
    
    # Method that generates the HTML webpage
    def generate_page(self):
        # Return a string containing HTML code
        # f""" means this is a formatted string (can insert variables)
        return f"""
        <html>
        <body>
        <h1> Smart Room Monitor </h1>
        <p> System Running </p>
        <p> Requests: {self.request_count} </p>
        </body>
        </html>
        """
    