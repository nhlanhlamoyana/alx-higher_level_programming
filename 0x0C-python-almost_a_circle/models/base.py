#!/usr/bin/python3
'''Module for Base class.'''



class Base:
    '''A repesentation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init_(self, id-None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
