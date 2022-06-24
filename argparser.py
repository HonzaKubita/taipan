from object import newObject # Library for creating anonymus objects
import sys
class argParser:
  def __init__(self, template): # Constructor
    self.template = template

  def parse(self):
    args = newObject() # Create a new oject
    for i, templateItem in enumerate(self.template):

      if '--options' in templateItem: # This item is a options section
        args.options = newObject()
        shellOptions = [s for s in sys.argv if "--" in s] # Extract options from shell arguments
        for key, value in self.options.__dict__.items():
          optionSpecified = f'--{key}' in shellOptions
          if value == 'bool': # Option type is bool
            args.options[key] = optionSpecified
          elif value == 'str': # Option type is string
            args.options[key] = sys.argv[sys.argv.index(f'--{key}') + 1] if optionSpecified else None # If specified put value else None

      else: # Normal argument
        try:
          sys.argv[i + 1]
          args[templateItem] = sys.argv[i + 1] # Put shell arguments into the object as their name and value
        except:
          args[templateItem] = None
    return args # Return the object
  