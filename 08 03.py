class Booking:

    price = 1000
    max_hours = 10
    
    def __init__(self, client_name, room, time):
        self.client_name = client_name
        self.room = room
        self.time = time

    def culc_cost(self):
        return self.time * self.price
        

booking1 = Booking("ivan", 2, 4)
booking2 = Booking("maria", 4, 6)

booking1.price = 800

print(booking1.culc_cost())
print(booking2.culc_cost())
