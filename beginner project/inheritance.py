class parent1:
    def show(self):
        print("this method is in  parent class")
class parent2():
    def show(self):
        print("this method is in  parent class 2 ")
class child(parent1,parent2):
    def method3(self):
        print("this method is in child class")
obj = child()
obj.show()
obj.show()
obj.method3()