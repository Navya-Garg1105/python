class parent1:
    def disp(self):
        print("print from class parent1")
class parent2:
    def disp(self):
        print("print from class parent2")
class A (parent1):
    def disp(self):
        print("method inside A")
        super().disp()
class B (parent2):
    def disp(self):
        print("method inside B")
class C(A,B):
    def disp(self):
        print("method inside C")
        super().disp()
obj = C()
obj.disp()
print(C.__mro__)