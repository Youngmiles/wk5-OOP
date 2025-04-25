class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed 
    
    def move(self):
        """Movement behavior to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement move()")
    
    def travel_time(self, distance):
        """Calculate travel time for given distance"""
        return f"{distance / self.speed:.1f} hours"

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        return f"{self.name} is driving on the road at {self.speed} km/h 🚗💨"
    
    def honk(self):
        return "Beep beep! 🚦"

class Airplane(Vehicle):
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude  
    
    def move(self):
        return f"{self.name} is flying at {self.speed} km/h (Altitude: {self.altitude}m) ✈️☁️"
    
    def take_off(self):
        return "🛫 Preparing for takeoff... Wheels up!"

class Boat(Vehicle):
    def __init__(self, name, speed, boat_type):
        super().__init__(name, speed)
        self.boat_type = boat_type
    
    def move(self):
        return f"{self.name} is sailing on water at {self.speed} km/h ⛵🌊"
    
    def anchor(self):
        return "Dropping anchor! ⚓"

class Train(Vehicle):
    def __init__(self, name, speed, carriages):
        super().__init__(name, speed)
        self.carriages = carriages
    
    def move(self):
        return f"{self.name} is chugging along the tracks at {self.speed} km/h (Carriages: {self.carriages}) 🚂🔔"
    
    def blow_whistle(self):
        return "Choo choo! 🚃"

class Bicycle(Vehicle):
    def __init__(self, name, speed, gears):
        super().__init__(name, speed)
        self.gears = gears
    
    def move(self):
        return f"{self.name} is pedaling at {self.speed} km/h (Gear: {self.gears}) 🚴💨"
    
    def ring_bell(self):
        return "Ring ring! 🔔"

fleet = [
    Car("Tesla Model 3", 120, "Electric"),
    Airplane("Boeing 747", 900, 12000),
    Boat("Sailfish 22", 25, "Sailboat"),
    Train("Shinkansen Bullet", 320, 16),
    Bicycle("Mountain Bike", 25, 7)
]

print(" 🚗 🚑 🚎 ✈ 🏍 Vehicle Simulator ")
for vehicle in fleet:
    print("\n" + vehicle.move())
    print(f"Time to travel 100 km: {vehicle.travel_time(100)}")
    
    if isinstance(vehicle, Car):
        print(vehicle.honk())
    elif isinstance(vehicle, Airplane):
        print(vehicle.take_off())
    elif isinstance(vehicle, Boat):
        print(vehicle.anchor())
    elif isinstance(vehicle, Train):
        print(vehicle.blow_whistle())
    elif isinstance(vehicle, Bicycle):
        print(vehicle.ring_bell())

print("\n Special Ops ")

spaceship = type("Spaceship", (Vehicle,), {
    "move": lambda self: f"{self.name} is launching into space at {self.speed} km/h 🚀🌌",
    "land": lambda self: "Re-entering atmosphere... 🔥"
})

falcon_heavy = spaceship("Falcon Heavy", 28000)
print(falcon_heavy.move())
print(falcon_heavy.land())
print(f"Time to reach Moon (384,400 km): {falcon_heavy.travel_time(384400)} hours")