class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    # Override this in Car
    def display_info(self):
        return f"{self.year} {self.model}"

class Car(Vehicle):
    def __init__(self, model, year, num_doors):
        # Initialize parent and add doors
        super().__init__(model,year)
        self.num_doors = num_doors
    
    # Implement this method
    def display_info(self):
        # Include num_doors in output
        return f'{self.year} {self.model}, {self.num_doors} doors '

# Test Input
car = Car("Toyota Camry", 2020, 4)
print(car.display_info())  # Expected Output: "2020 Toyota Camry, 4 doors"