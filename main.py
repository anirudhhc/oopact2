#create class
class vehicle:

    #create init function
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage

#creating object
mode=vehicle(200,14)

#aceesing
print("Model Max Speed:",mode.max_speed)
print("Model mileage",mode.mileage)


        
        