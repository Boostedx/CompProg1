from circle import Circle
from rect import Rect

circle = Circle(radius=5)
rectangle = Rect(length=10, width=5)

# 1
print('The area of the circle is {0}. The area of the rectangle is {1}. '
      .format(str(circle.circ_area()), str(rectangle.rect_area())))

# 2
print('The circumference of the circle is : ' + str(circle.circ_circum()))

# 3
print('The circumference of the rectangle is : ' + str(rectangle.rect_perim()))
