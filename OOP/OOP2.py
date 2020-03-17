# Object Oriented Programming in Python according to ZyBooks

# Seat Reservation 

class Seat:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def reserve(self, fn, ln, pd):
        self.first_name = fn
        self.last_name = ln
        self.paid = pd

    def make_empty(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ''

    def print_seat(self):
        print('%s %s, Paid: %.2f' % (self.first_name, self.last_name, self.paid))


def make_seats_empty(seats):
    for s in seats:
        s.make_empty()


def print_seats(seats):
    for s in range(len(seats)):
        print('%d:' % s, end=' ')
        seats[s].print_seat()

# Racing
class RaceTime:

    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        print('Time to complete race: %d:%d' % (hours, minutes))

    def print_pace(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        total_minutes = hours*60 + minutes
        print('Avg pace (mins/mile): %.2f' % (total_minutes / self.distance))

# Inheritance
class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        print(self.name, self.quantity)


class Produce(Item):  # Derived from Item
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.expiration = ''

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration

# Transportation
class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print('%s can go %d mph.' % (self.name, self.speed))

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0 

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print('%f gallons remaining.' % self.fuel_gal)

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')

def main():
    # Seat Reservation
    num_seats = 5

    available_seats = []
    for i in range(num_seats):
        available_seats.append(Seat())

    command = input('Enter command (p/r/q): ')
    while command != 'q':
        if command == 'p':  # Print seats
            print_seats(available_seats)
        elif command == 'r':  # Reserve a seat
            seat_num = int(input('Enter seat num:\n'))
            if not available_seats[seat_num].is_empty():
                print('Seat not empty')
            else:
                fname = input('Enter first name:\n')
                lname = input('Enter last name:\n')
                paid = float(input('Enter amount paid:\n'))
                available_seats[seat_num].reserve(fname, lname, paid)
        else:
            print('Invalid command.')

        command = input('Enter command (p/r/q):\n')

    # Racing
    distance = 5.0

    start_hrs = int(input('Enter starting time hours: '))
    start_mins = int(input('Enter starting time minutes: '))
    end_hrs = int(input('Enter ending time hours: '))
    end_mins = int(input('Enter ending time minutes: '))

    race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

    race_time.print_time()
    race_time.print_pace()

    # Produce and Inheritance
    item1 = Item()
    item1.set_name('Smith Cereal')
    item1.set_quantity(9)
    item1.display()

    item2 = Produce()
    item2.set_name('Apples')
    item2.set_quantity(40)
    item2.set_expiration('May 5, 2012')
    item2.display()
    print('  (Expires:(%s))' % item2.get_expiration())

    scooter = MotorCycle('Vespa', 55, 40)
    dirtbike = MotorCycle('KX450F', 80, 25)

    scooter.info()
    dirtbike.info()
    choice = input('Select scooter (s) or dirtbike (d): ')
    bike = scooter if (choice == 's') else dirtbike

    menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
    command = input(menu)
    while command != 'q':
        if command == 'f':
            fuel = int(input('Enter amount: '))
            bike.add_fuel(fuel)
        elif command == 'g':
            distance = int(input('Enter distance: '))
            bike.drive(distance)
        elif command == 'w':
            bike.wheelie()
        elif command == 'q':
            break
        else:
            print('Invalid command.')

        command = input(menu)
        

main()




