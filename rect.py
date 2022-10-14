class Rect:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rect_area(self):
        return (self.length * self.width)
    def rect_perim(self):
        return ((self.length + self.width) * 2)


