'''
Title:Example for Single Inheritance
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
        print('\nDefault Constructor: Class B')
        return

    def __del__(self):
        print('\nDestructor : Class B')
        return

B()

'''
output:

Default Constructor: Class B

Destructor : Class B

'''
