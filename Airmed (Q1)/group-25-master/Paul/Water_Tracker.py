#Water Tracker Draft

#Features to implement:
# - Time tracking to display graph of water consumption over the course of one day
# - An actual functioning menu
# - Proper user interface (instead of "press '1' "etc.)
# - Adding different kinds of drinks (like beer/wine/juice/milk/soft_drinks/spirits etc.)
# - Adding hydrating fruits like water melon






def waterIn():
    wIn  = raw_input("How many ml of water did you drink? "))
    return int(wIn)

def giveStats(ttl):


    waterttl = ttl

    print("An average person should drink 2 liters of water a day, \n you drank {}% of your daily intake so far."
          .format((waterttl/2000)*100))

    #Return not really implemented
    end = input("Press '1' to return: ")
    end == 1:
        Water_tracker()



    
def Water_Tracker():
    
    with open("water.txt","r") as f:
        val = f.readlines()
        if val != "":
            if val != 0:
                ttl = val
            else:
                ttl = 0
        else:
            ttl = 0
    
    inputting = True

    while inputting:
        want = raw_input("Drank more? Press '1' to add water, press '2' to see stats, press '3' to quit: "))
        if want == 1:
            ttl += waterIn()
            with open("water.txt","w") as f:
                f.write(ttl)
                f.close()
        elif want == 2:
            giveStats(ttl)
        elif want == 3:
            inputting = False
        else:
            continue
    #Return to main menu not implemented


def keepTime(oldsec):
    import time
    newsec = time.time()
    sec = newsec - oldsec
    return sec / 3600


def waterIn():
    wIn = raw_input("How many ml of water did you drink? "))
    return int(wIn / 1000)


def waterHad():
    with open("water.txt", "r") as f:
        val = f.readlines()
        if val != "" or val != 0: ttl = val
        f.close()
    else: ttl = 0
    f.close()


return ttl


def waterHaving(ttl):
    with open("water.txt", "w") as f: f.write("\n" + ttl)
    f.close()
    return


def plot(x, y):
    import matplotlib.pyplot as plt
    plt.plot(x, y, 'bo')
    plt.title('Water Intake over the last 24 Houres')
    plt.grid(True)
    plt.xlabel("Houres")
    plt.ylabel("Liters")
    plt.show()


class Person():
    def __init__(self):
        self._object = None

    def _initialize(self, name):
        self._object = {'name': name
                        }

    def add_property(self, key, value):
        self._object[key] = value


class Water_tracker(Person):
    def __init__(self):
        super().__init__(self)

    def

        # General User Framework for importing functions to be
        # used by different programmes

        class NewUser(password, username, email):

            def __init__(self, password, username, email):
                self.password = password
                self.username = username
                self.email = email
                self.data = {}

            def setData(self, id, data):
                self.data[id] = data

            def waterTracker(self):
                id = 'water'
                current_data = self.data[id]
                data = raw_input("Enter amount of water: ")
                setData(self, id, (data + current_data))

            # Create a new user

            def initialize():
                # Get user data
                name = str(input("Enter username: "))
                age = int(input("Enter your age: "))
                weight = int(input("Enter your weight: "))
                return name, age, weight

            def logUser(name, age, weight):
                # Safe user data to "Users.txt" File
                with open("Users.txt", "w") as f:
                    f.write("{};{};{}"
                            .format(name, age, weight))
                    f.close()

            # Call functions to "create" new user
            name, age, weight = initialize()
            logUser(name, age, weight)

        def UserData(key):
            # Retrieve user data from log file

            with open("Users.txt", "r") as f:
                lines = f.readlines()
                found = False
                while not found:
                    for line in lines:
                        if key in line:
                            name, age, weight = line.split(";")
                            found = True
                            return [name, int(age), int(weight)]






