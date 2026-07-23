class dog:
    
    def __init__(self):
        self.Health=100
        self.Hunger=50
        self.Life=0
        self.Energy=50
        self.Happyness=50
    def feed(self):
        self.Hunger -= 10
        if(self.Hunger<0):
            self.Health -=50
            self.Energy -=50
        self.Life +=1

        
       
