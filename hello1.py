class A:
    def __init__(self):
        self.a="hello"
    
    def print_fun(self):
        print(self.a+"world")


if __name__=="__main__":
    b=A()
    b.print_fun()
    c=A()
    c.print_fun()
