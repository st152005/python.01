def usquare(a):
    return a*a

def ucube(a):
    print(a*a*a)
    return


class UCompute:

    def readFloat(self):
        try:
            self.x=float(input('Enter x value:'))
        except:
            self.x=0
            return

        try:
            self.y=float(input('Enter y value:'))
        except:
            self.y=0
            return


    def udiv(self):
        return self.x/self.y

    def umod(self):
        print(self.x % self.y)
        return
    



    
