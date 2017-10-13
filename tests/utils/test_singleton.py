import random

from lib.utils.singleton import Singleton

def test_singleton():
    ''' Tests the singleton metaclass. '''

    class RandomPropClass(metaclass=Singleton):

        def __init__(self):
            self.property = random.randint(0, 9)

        def get_property(self):
            return self.property

    
    n = 0
    while n < 10:
        ''' Over 10 iterations, the  RandomPropClass should always work with  the same random num '''
        instance_1 = RandomPropClass()
        instance_2 = RandomPropClass()

        n = n + 1

        assert instance_1.get_property() == instance_2.get_property()
