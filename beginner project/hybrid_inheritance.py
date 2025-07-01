class base:
    def method1(self):
        print("method in base class")
class child1(base):
    def method2(self):
        print("method in child1 class")
class child2(base):
    def method3(self):
        print("method in child 2 class")
class grandchild(child1,child2):
    def method4(self):
        print("method in grandchild class")
obj = grandchild()
obj.method1()
obj.method2()
obj.method3()
obj.method4()
