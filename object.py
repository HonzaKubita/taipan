class newObject:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
  def __setitem__(self, key, value):
    self.__dict__[key] = value
