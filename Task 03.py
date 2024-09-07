class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.state = "stopped"  

    def start(self):
        if self.state == "started":
            print(f"The {self.brand} {self.model} is  Alreadystarted.")
        else:
             self.state = "started"
             print(f"The {self.brand} {self.model} is started.")

    def stop(self):
        if self.state == "stopped":
           print(f"The {self.brand} {self.model} is Already stopped.")
        else:
            self.state = "stopped"
            print(f"The {self.brand} {self.model} is stopped.")

    def __str__(self):
        return f"{self.brand} {self.model} (State: {self.state})"
cars = []
def find_car(brand, model):
    for car in cars:
        if car.brand == brand and car.model == model:
            return car
    return None

def main():
    while True:
        command = input(" Enter(add) to add a car:\n Enter(start) to start a car:\n Enter (stop)to stop a car:\n Enter (exit)to exit a car:\n Enter your command:")
                    
         
        if command == "add":
            brand = input("Enter car brand: ")
            model = input("Enter car model: ")
            car = Car(brand, model)
            cars.append(car)
            print(f"Added {car}.")
        elif command.startswith("start "):
            _, brand, model = command.split(maxsplit=2)
            car = find_car(brand, model)
            if car:
                car.start()
            else:
                print(f"Not found.")
        elif command.startswith("stop "):
            _, brand, model = command.split(maxsplit=2)
            car = find_car(brand, model)
            if car:
                car.stop()
            else:
                print(f"Not found.")
        if command == "exit":
            print("Bye....")

if __name__ == "__main__":
    main()
