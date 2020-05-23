class Circle:
    '''
    A class definition that has  two methods which computes the Circumference and 
    Area of a circle of the radius passed in respectively.
    '''
    def __init__(self, radius):
        self.radius = radius

    def computeCircum(self):
        return f'{int(round(2*22/7*self.radius, 0))}cm'

    def computeArea(self):
        return f'{int(round(22/7 * self.radius**2))}cm2'

a = Circle(7)
print(a.computeCircum())