'''
Title: How to develop exam result exercise using Object Based Programing Language
'''

class ExamResult:
    def setData(self):
        self.rno=int(input("Enter Roll No.:"))
        self.sname=input("Enter Student Name:")
        self.m1=float(input("Mark-1:"))
        self.m2=float(input("Mark-2:"))
        return
    def computeData(self):
        self.total=self.m1+self.m2
        self.avg=self.total/2
        self.result='Fail'
        if self.m1>34.4 and self.m2>34.4:
            self.result='Pass'
            return
    def showData(self):
        self.computeData()

        print('Roll no:%d'%(self.rno))
        print('Student Name:%s'%(self.sname))
        print('Mark-1:%2f'%(self.m1))
        print('Mark-2:%2f'%(self.m2))
        print('Total:%2f'%(self.total))
        print('Average:%2f'%(self.avg))
        print('Result:%s'%(self.result))

obj=ExamResult()

obj.setData()
obj.showData()

'''
Output-01:

Enter Roll No.:1001
Enter Student Name:x5
Mark-1:56.5
Mark-2:63

Roll no:1001
Student Name:x5
Mark-1:56.50
Mark-2:63.00
Total:119.50
Average:59.75
Result:Pass

Output-02:

Enter Roll No.:1002
Enter Student Name:x4
Mark-1:80
Mark-2:20

Roll no:1002
Student Name:x4
Mark-1:80.00
Mark-2:20.00
Total:100.00
Average:50.00
Result:Fail

'''
        
        
