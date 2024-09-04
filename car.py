car_started = False
while True:
    car= input("Enter 'start' to start the car or \n Enter 'stop' to stop the car  or \n Enter 'quit' to exit: ")
    
    if car == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started.")
    
    elif car == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("Car stopped.")
    
    elif car == "quit":
        print("byee...")
        break
    
-0   
