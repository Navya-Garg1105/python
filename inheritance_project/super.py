class a:
    def disp(self):
        print("print from a")
class b(a):
    def disp(self):
        print("print from b")
        super().disp()
obj = b()
obj.disp()
print(b.__mro__)