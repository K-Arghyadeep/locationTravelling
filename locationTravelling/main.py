from cities import Location
from transportation import Tranportation_Mode
from transportation import Train
from transportation import Bus
from transportation import Auto
from transportation import Metro


locations = {
        "A": Location("A", attractions=["Attraction A1", "Attraction A2"], connected_to=("B","C")),
        "B": Location("B", connected_to=("A","D")),
        "C": Location("C", attractions=["Attraction C1", "Attraction C2"], connected_to=("A","E")),
        "D": Location("D", connected_to=("B","E")),
        "E": Location("E", connected_to=("D","C"))
    }

transportation_modes = {
    "bus" : Tranportation_Mode("Bus", routes=["81", "81/1"]),
    "train" : Tranportation_Mode("Train", routes=["SDH-BKP", "BKP-SDH"]),
    "metro" : Tranportation_Mode("Metro", routes=["South", "East-West"]),
    "auto" : Tranportation_Mode("Auto", routes=["AT1", "12/C"]),
}

train_routes = {
    "route_1" : Train("SDH-BKP", stops=["A", "C"]),
    "route_2" : Train("BKP-SDH", stops=["C", "D"])
}

bus_routes = {
    "route_1" : Bus("81", stops=["A", "B"]),
    "route_2" : Bus("81/1", stops=["B", "E"])
}

auto_routes = {
    "route_1" : Auto("AT1", stops=["B", "C"]),
    "route_2" : Auto("12/C", stops=["C", "D"])
}

metro_routes = {
    "route_1" : Metro("South", stops=["B", "D"]),
    "route_2" : Metro("East-West", stops=["D", "E"])
}


def transport_suggestion(start_location, destination):
    if start_location not in locations or destination not in locations:
        return f"Invalid location"

    flag = False

    for route, train in train_routes.items():
        if start_location in train.stops and destination in train.stops:
            flag = True
            print(f"Take train {train_routes[route].route} from {start_location} to {destination}")

    for route, bus in bus_routes.items():
        if start_location in bus.stops and destination in bus.stops:
            flag = True
            print(f"Take train {bus_routes[route].route} from {start_location} to {destination}")

    for route, auto in auto_routes.items():
        if start_location in auto.stops and destination in auto.stops:
            flag = True
            print(f"Take train {auto_routes[route].route} from {start_location} to {destination}")

    for route, metro in metro_routes.items():
        if start_location in metro.stops and destination in metro.stops:
            flag = True
            print(f"Take train {metro_routes[route].route} from {start_location} to {destination}")

    if flag == False:
        pass

start, dest = input("start_location destination").split()
transport_suggestion(start_location=start, destination=dest)