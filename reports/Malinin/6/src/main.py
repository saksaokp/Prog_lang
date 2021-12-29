class gorod:
    cout = 0
    name = str()
    nas = int()
    area = int()
    data = int()




    def __init__(self):
        gorod.count += 1
        print(gorod.count)

    def __init__(self, name="", nas=0, area=0, data="noy"):
        self.name = name
        self.nas = nas
        self.area = area
        self.data = data

    def set_name(self,nm):
        self.name = nm

    def set_nas(self,ns):
        self.nas = ns

    def set_area(self,ar):
        self.area = ar

    def set_data(self,dt):
        self.data = dt

    def get_name(self):
        return self.name

    def get_nas(self):
        return self.nas

    def get_area(self):
        return self.area

    def get_data(self):
        return self.data

    def read(self):
        self.name = str(input("\nEnter name:"))
        self.nas = str(input("\nEnter nas:"))
        self.area = str(input("\nEnter area:"))
        self.data = str(input("\nEnter data:"))

    def show(self):
        print("Name-" + self.name + "; Naselenie: " + str(self.nas) + "; area " + str(self.area) + "; Data-" + str(self.data))

one = gorod()
two = gorod("Brest",300000,1,1901)
one.read()
one.show()
two.show()





