class Location:
    def __init__(self, name, attractions=None, connected_to=None):
        self.name = name
        self.attractions = attractions if attractions else []
        self.connected_to = connected_to if connected_to else ()

    def __str__(self):
        return f"Location: {self.name}, Attractions: {', '.join(self.attractions)}"

