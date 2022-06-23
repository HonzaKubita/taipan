from object import newObject # Library for creating anonymus objects
import sys
class argParser:
  def __init__(self, template): # Constructor
    self.template = template

  def parse(self):
    args = newObject() # Create a new oject
    for i, item in enumerate(self.template):
      args[item] = sys.argv[i + 1] # Put shell arguments into the object as their name and value
    return args # Return the object
  