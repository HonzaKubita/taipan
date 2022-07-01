import math as m
class Loading:
  def __init__(self, capacity, size=20, border="[]", fill="█", empty="."):
    self.filled = 0
    self.capacity = capacity
    self.size = size
    self.r_border = border[:len(border)//2]
    self.l_border = border[len(border)//2:]
    self.fill = fill
    self.empty = empty

  def _render(self, clear=True):
    if clear:
      print (f"\033[A    {'  ' * self.size}     \033[A") # Delete last line
    # capacity 10
    # filled 5
    percentage = self.filled / self.capacity
    percentageFill = m.floor(percentage * self.size)
    print(f'{ self.r_border }{ self.fill * percentageFill }{ self.empty * ( self.size - percentageFill ) }{ self.l_border }')

  def start(self):
    self._render(False)

  def add(self, amount):
    self.filled += amount
    self._render()

  def remove(self, amount):
    self.filled -= amount
    self._render()
