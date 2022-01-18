'''
Playground for testing Pylint.
'''
class Car:
    '''
    Object which represents real world cars.
    '''
    def __init__(self,color:str) -> None:
        self.color = color

    def change_color(self,color: str) -> None:
        '''
        Sets new color of Car.
        '''
        self.color = color

my_car = Car('blue')
#pylint: disable=unused-argument
def crash(car1,car2):
    '''
    Example function.
    '''
    car1.color = 'burnt'
crash(Car('red'), my_car)
