country="INDIA"
class ace:
    clg="ACE ENGINEERING COLLEGE "
    def give(self,a,b,c,d,e):
        self.avg=(a+b+c+d)/4
        self.name=e
    def display(self):
        print("Name:",self.name)
        print("average=",self.avg)
        print("College =",ace.clg)
        print("Country =",country)
class bvrit:
    clg="BVRIT COLLEGE"
    def give(self,a,b,c,d,e):
        self.avg=(a+b+c+d)/4
        self.name=e
    def display(self):
        print("Name:",self.name)
        print("average=",self.avg)
        print("College =",ace.clg)
        print("Country =",country)
        
    
a=ace()
a1=ace()
b=bvrit()
b1=bvrit()
a.give(100,20,50,80,"Naresh")
a1.give(90,70,20,50,"Suresh")
b.give(75,25,70,50,"sita")
b1.give(95,65,50,78,"gita")
a.display()
a1.display()
b.display()
b1.display()

