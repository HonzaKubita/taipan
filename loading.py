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
    self.description = ""

  def _render(self):
    # capacity 10
    # filled 5
    percentage = self.filled / self.capacity
    percentageFill = m.floor(percentage * self.size)
    print(f'{ self.r_border }{ self.fill * percentageFill }{ self.empty * ( self.size - percentageFill ) }{ self.l_border } {m.floor(percentage * 100)}% {self.description}', end = '\r' if self.filled < self.capacity else '\n')

  def start(self):
    self._render()

  def add(self, amount):
    self.filled += amount
    self._render()

  def remove(self, amount):
    self.filled -= amount
    self._render()

  def addDescription(self, description):
    self.description = description
    self._render()
