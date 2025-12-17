class UCalc:

    def __init__(self):
        print('\nDefault Constructor')
        self.x=0
        self.y=0
        return

    def readInt(self):
        try:
            self.x=int(input('Enter x value:'))
        except:
            self.x=0

        try:
            self.y=int(input('Enter y value:'))
        except:
            self.y=0
            return

    def readFloat(self):
        try:
            self.x=float(input('Enter x value:'))
        except:
            self.x=0

        try:
            self.y=float(input('Enter y value:'))
        except:
            self.y=0
            return

    def __del__(self):
        del self.x,self.y
        print('\nDestructor processing...')
        return

    def usum(self):
        return self.x+self.y

    def uproduct(self):
        print(self.x * self.y)
        return
    
