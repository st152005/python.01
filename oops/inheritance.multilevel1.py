'''
Title:Example for Multilevel Inheritance
'''

class A:

    def __init__(self):
        print('\nDefault Constructor: Class A')
        return

    def __del__(self):
        print('\nDestructor : Class A')
        return

class B (A):

    def __init__(self):
        self.objA=A()
        print('\nDefault Constructor: Class B')
        return

    def __del__(self):
        print('\nDestructor : Class B')
        del self.objA
        return

class C (B):

    def __init__(self):
        self.objB=B()
        print('\nDefault Constructor: Class C')
        return

    def __del__(self):
        print('\nDestructor : Class C')
        del self.objB
        return
C()

'''
output:

Default Constructor: Class A

Default Constructor: Class B

Default Constructor: Class C

Destructor : Class C

Destructor : Class B

Destructor : Class A

'''
