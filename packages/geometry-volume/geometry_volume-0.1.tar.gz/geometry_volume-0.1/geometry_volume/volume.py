import math

class volume():
    def cone(radius,height):
        return round(radius**2*height*math.pi/3,2)

    def cylinder(radius,height):
        return round(radius**2*height*math.pi,2)

    def rectangular_prism(length,width,height):
        return length*width*height

    def cube(side):
        return side**3

    def others(base,height):
        return base*height

    def pyramid(length,width,height):
        return round(length*width*height/3,2)

    def triangular_prism(length,width,height):
        return length*width/2*height

    def trapezoidal_prism(base,top,length,height):
        return (base+top)*length/2*height

    def sphere(radius):
        return round(radius**3 * math.pi * 4/3,2)