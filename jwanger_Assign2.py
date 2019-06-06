#------------------------------------------------------------------------------------------------
# By: Jakob Wanger
# Description: This program will prompt the user to pick a shape and then enter its
#              dimensions to calculate its volume. The user then has the ability to
#              continue entering shapes and their dimensions or to quit the program
#              and see all the volumes for each shape displayed in ascending order.
#------------------------------------------------------------------------------------------------


import math
def main ():
    cubeVolumeList= [] #Storing the Cube Volumes
    pyramidVolumeList= [] #Storing the Pyramid Volumes
    ellipsoidVolumeList= [] #Storing the Ellipsoid Volumes
    keepLooping=True #Storing if the user has quit True= Not Quit, False= Quit


    while(keepLooping== True): #While User has more shapes continue
        shape= input("Please Enter the shape you would like to find the area for: ")

        upperShape=shape.upper() #converting it to upper case
        if (upperShape== "CUBE"): #If its a cube
            sideLength= (input("Please Enter the side Length of the Cube: "))
            if (sideLength.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(sideLength) #If not a number show invalid input output
            sideLength= float(sideLength)
            cubeVolumeList.append(cubeVolume(sideLength)) #Call on method to calulate the volume and store the answer in list

        elif (upperShape== "PYRAMID"):
            base=(input("Please Enter the Base of the Pyramid: "))
            if (base.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(base)
            base= float(base)
            height=(input("Please Enter the Height of the Pyramid: "))
            if (height.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(height)
            height= float(height)
            pyramidVolumeList.append(pyramidVolume(base,height)) #Call on method to calulate the volume and store the answer in list
        elif (upperShape== "ELLIPSOID"):
            radius1=(input("Please Enter the 1st Radius of the Ellipsoid: "))
            if (radius1.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(radius1)
            radius1=float(radius1)
            radius2=(input("Please Enter the 2nd Radius of the Ellipsoid: "))
            if (radius2.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(radius2)
            radius2=float(radius2)
            radius3=(input("Please Enter the 3rd Radius of the Ellipsoid: "))
            if (radius3.isdigit())==False: #Make sure the side length is a number to make sure no crahses in the program
                invalidInput(radius3)
            radius3=float(radius3)
            ellipsoidVolumeList.append(ellipsoidVolume(radius1,radius2,radius3)) #Call on method to calulate the volume and store the answer in list

        elif (upperShape== "QUIT"): #If the user is done inputting shapes
            print("")
            print("You have come to the end of the session.")
            if (len(cubeVolumeList)!=0 or len(pyramidVolumeList)!=0 or len(ellipsoidVolumeList)!=0 ): #Checks to see if the lists are empty i.e. no data
                #Sorting the lists
                cubeVolumeList.sort()
                pyramidVolumeList.sort()
                ellipsoidVolumeList.sort()

                #Printing the lists
                print("The volumes calculated for each shape are shown below")
                if len(cubeVolumeList)==0: #used to keep format in tact with empty lists
                    print("Cube: No computions for this shape")
                else:
                    print("Cube:", end=" ")

                for element in range (0,len(cubeVolumeList)):
                    if element==(len(cubeVolumeList)-1):
                        print(cubeVolumeList[element])
                    else:
                        print(cubeVolumeList[element], end=", ")

                if len(pyramidVolumeList)==0: #used to keep format in tact with empty lists
                    print("Pyramid: No computions for this shape")
                else:
                    print("Pyramid:", end=" ")

                for element in range (0,len(pyramidVolumeList)):
                    if element==(len(pyramidVolumeList)-1):
                        print(pyramidVolumeList[element])
                    else:
                        print(pyramidVolumeList[element], end=", ")
                if len(ellipsoidVolumeList)==0: #used to keep format in tact with empty lists
                    print("Ellipsoid: No computions for this shape")
                else:
                    print("Ellipsoid:", end=" ")
                    for element in range (0,len(ellipsoidVolumeList)):
                        if element==(len(ellipsoidVolumeList)-1):
                            print(ellipsoidVolumeList[element])
                        else:
                            print(ellipsoidVolumeList[element], end=", ")
            else:
                print("You did not perform any volume calculations")
            keepLooping=False

        else:
            invalidInput(shape)

def invalidInput (invalid): #Used to show the user that the input was valid and closes program
    print("I am sorry but",invalid, "is not a valid input. Goodbye")
    exit()

def cubeVolume(sideLength): #Used to calculate and return the volume of a cube
    volume= sideLength**3.0
    volume= round(volume,1)
    print("The Volume of a Cube with a side length of", sideLength, "is", volume)
    return volume

def pyramidVolume (base, height): #Used to calculate and return the volume of a pyramid
    volume= (1/3)*height*base**2
    volume= round(volume,1)
    print("The Volume of a Pyramid with a base of", base, "and a height of",height,"is", volume)
    return volume

def ellipsoidVolume (r1, r2, r3): #Used to calculate and return the volume of a ellipsoid
    PI=math.pi
    volume= (4/3)*PI*r1*r2*r3
    volume= round(volume,1)
    print("The Volume of a Ellipsoid with a radius' of {}, {}, and {} is {}".format(r1,r2,r3,volume))
    return volume

main() #Calls on the main method to begin the program
