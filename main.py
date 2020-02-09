# Import functions cubeVolume, pyramidVolume, and ellipsoidVolume for use in main function
from volumes import cubeVolume, pyramidVolume, ellipsoidVolume

# Empty lists to store newly calculated cube, pyramid and ellipsoid volumes
cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []

# Main function
# @userInput is the user's shape input, invalid input or quit input
# Calls the cubeDimensions, pyramidDimensions, and ellipsoidDimensions functions, and calculates shape volume
# Appends newVolume to cubeVolumeList, pramidVolumeList, or ellipsoidVolumeList depending on previous shape input
# When user quits the program, prints all volumes calculated for each shape.
def main():
    count = 0
    userInput = str(input("What shape do you want to calculate volume for (cube,c; pyramid,p; ellipsoid,e)?\nAlternatively if you want to quit enter (quit,q) ")).lower()
    while userInput not in ("quit", "q"):
        if userInput in ("cube", "c"):
            newVolume = cubeDimensions()
            count = count + 1
            cubeVolumeList.append(newVolume)
            userInput = str(input("What shape do you want to calculate volume for (cube,c; pyramid,p; ellipsoid,e)?\nAlternatively if you want to quit enter (quit,q) ")).lower()
        elif userInput in ("pyramid", "p"):
            newVolume = pyramidDimensions()
            count = count + 1
            pyramidVolumeList.append(newVolume)
            userInput = str(input("What shape do you want to calculate volume for (cube,c; pyramid,p; ellipsoid,e)?\nAlternatively if you want to quit enter (quit,q) ")).lower()
        elif userInput in ("ellipsoid", "e"):
            newVolume = ellipsoidDimensions()
            count = count + 1
            ellipsoidVolumeList.append(newVolume)
            userInput = str(input("What shape do you want to calculate volume for (cube,c; pyramid,p; ellipsoid,e)?\nAlternatively if you want to quit enter (quit,q) ")).lower()
        else:
            print("Please enter a valid input.")
            userInput = str(input("What shape do you want to calculate volume for (cube,c; pyramid,p; ellipsoid,e)?\nAlternatively if you want to quit enter (quit,q) ")).lower()
    if userInput in ("quit", "q") and count == 0:
        print("You have reached the end of your session\nYou did not perform any volume calculations.")
        quit()
    elif userInput in ("quit", "q") and count > 0:
        print("You have reached the end of your session\nThe volumes calculated for each shape are: ")
        finalCubeVolumes()
        finalPyramidVolumes()
        finalEllipsoidVolumes()
        quit()
    return


# Calculates cube volume based on user's input dimensions
# @sideInput is the user's side length input for the cube
# @return calculated cube volume
def cubeDimensions():
    sideInput = int(input("Enter a value for the side length of the cube: "))
    calculatedVolume = cubeVolume(sideInput)
    calculatedVolume = round(calculatedVolume, 2)
    return calculatedVolume

# Calculates pyramid volume based on user's input dimensions
# @baseInput is the user's base length input for the cube
# @heightInput is the user's height input for the cube
# @return calculated pyramid volume
def pyramidDimensions():
    baseInput = int(input("Enter a value for the base of the pyramid: "))
    heightInput = int(input("Enter a value for the height of the pyramid: "))
    calculatedVolume = pyramidVolume(baseInput, heightInput)
    calculatedVolume = round(calculatedVolume, 2)
    return calculatedVolume

# Calculates ellipsoid volume based on user's input dimensions
# @r1Input is the user's first radius input for the cube
# @r2Input is the user's second radius input for the cube
# @r3Input is the user's third radius input for the cube
# @return calculated ellipsoid volume
def ellipsoidDimensions():
    r1Input = int(input("Enter a value for r1 of the ellipsoid: "))
    r2Input = int(input("Enter a value for r2 of the ellipsoid: "))
    r3Input = int(input("Enter a value for r3 of the ellopsoid: "))
    calculatedVolume = ellipsoidVolume(r1Input, r2Input, r3Input)
    calculatedVolume = round(calculatedVolume, 2)
    return calculatedVolume

# Prints all cube volumes calculated before user quits.
def finalCubeVolumes():
    cubeVolumeList.sort()
    if cubeVolumeList == []:
        print("Cube: No shapes entered")
    else:
        print("Cube: ", str(cubeVolumeList).strip("[]"))

# Prints all pyramid volumes calculated before user quits.
def finalPyramidVolumes():
    pyramidVolumeList.sort()
    if pyramidVolumeList == []:
        print("Pyramid: No shapes entered")
    else:
        print("Pyramid: ", str(pyramidVolumeList).strip("[]"))

# Prints all ellipsoid volumes calculated before user quits.
def finalEllipsoidVolumes():
    ellipsoidVolumeList.sort()
    if ellipsoidVolumeList == []:
        print("Ellipsoid: No shapes entered")
    else:
        print("Ellipsoid: ", str(ellipsoidVolumeList).strip("[]"))

# Call main function to initiate the program
main()
