# Import pi for use in ellipsoidVolume function
from math import pi

# Computes the volume of a cube
# @param side is the length of a side of the cube
# @return volume
def cubeVolume(side):
    volume = side**3
    print("The volume of a cube with side length = %d is: %.2f" %(side, volume))
    return volume

# Computes the volume of a pyramid
# @param base is the base length of the pyramid
# @param height is the height of the pyramid
# @return volume
def pyramidVolume(base, height):
    volume = (1/3)*(base**2)*height
    print("The volume of a pyramid with base length = %d and height = %d is: %.2f" %(base, height, volume))
    return volume

# Computes the volume of an ellipsoid
# @param r1 is radius 1 of the ellipsoid
# @param r2 is radius 2 of the ellipsoid
# @param r3 is radius 3 of the ellipsoid
# @return volume
def ellipsoidVolume(r1, r2, r3):
    volume = (4/3)*pi*r1*r2*r3
    print("The volume of an ellipsoid with r1 = %d, r2 = %d, and r3 = %d is: %.2f" %(r1, r2, r3, volume))
    return volume

