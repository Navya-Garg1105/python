class grandparent:
    def method1(self):
        print("grandparent class")
class parent(grandparent):
    def method1(self):
        print("parent child")
class child(parent):
    def method3(self):
        print("child class")
obj = child()
obj.method1()
obj.method1()
obj.method3()
