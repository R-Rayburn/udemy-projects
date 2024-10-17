class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    # todo
    return f'A circle of radius {self.radius}'

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    # todo
    return f'A square with side {self.side}'


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    # todo
    if isinstance(self.shape, Circle):
        self.shape.resize(factor)
    # note that a Square doesn't have resize()

  def __str__(self):
    # todo
    return f"{self.shape} has the color {self.color}"