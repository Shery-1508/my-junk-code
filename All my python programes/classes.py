
class mainclass():
    def func1(self):
        print("This is function\n")

    def func2(self,str1):
        print("You Entered this is string \" ", str1 , ' "  ')


class derivedclass(mainclass):
    def func3(self):
        print("This is derived function\n")
        self.func1()

a = mainclass()




a.func1()
a.func2("test string\n")
b = derivedclass()

b.func1()
b.func2("derived\n")
b.func3()
