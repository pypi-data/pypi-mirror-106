from .attribute import Attribute


class Tag(object):
    def __init__(self, name):
        self.name = name
        self.attributes = []
        
    def add_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)
