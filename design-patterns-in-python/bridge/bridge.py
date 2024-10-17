# Have drawing application that can draw
# circle, square
# in different forms (vector, raster)
# Need nice api to draw them

# VectorCircle, VectorSquare, RasterCircle, RastaSquare
# Complex and explodes in classes when new ones are added.

# Need to make a connection with a shape and the renderer

from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass
    def render_square(self, radius):
        pass
    # render_triangle

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
    def draw(self):
        # Bridge connection to renderer
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

