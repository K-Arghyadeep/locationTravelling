class Tranportation_Mode:
    def __init__(self, type, routes=None):
        self.type = type
        self.routes = routes if routes else []

    def __str__(self):
        return f"Transport Mode: {self.type}, Routes: {', '.join(self.routes)}"


class Train:
    def __init__(self, route, stops=None):
        self.route = route
        self.stops = stops if stops else []

    def __str__(self):
        return f"Route Number: {self.route}, Stops: {', '.join(self.stops)}"


class Bus:
    def __init__(self, route, stops=None):
        self.route = route
        self.stops = stops if stops else []

    def __str__(self):
        return f"Route Number: {self.route}, Stops: {', '.join(self.stops)}"


class Auto:
    def __init__(self, route, stops=None):
        self.route = route
        self.stops = stops if stops else []

    def __str__(self):
        return f"Route Number: {self.route}, Stops: {', '.join(self.stops)}"


class Metro:
    def __init__(self, route, stops=None):
        self.route = route
        self.stops = stops if stops else []

    def __str__(self):
        return f"Route Number: {self.route}, Stops: {', '.join(self.stops)}"
