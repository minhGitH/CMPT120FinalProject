# Header
# Group 143
# Savan Kajo (301464034)
# Tuan Minh Le Nguyen (301539625)
# Final Project



import cmpt120image
import cmpt120colours

def hexNumbers(r,g,b): ### to convert decimal to hexadecimal
    red = int(r)
    green = int(g)
    blue = int(b)

    red = hex(red)
    green = hex(green)
    blue = hex(blue)

    redHex = red.replace('0x','')
    greenHex = green.replace('0x','')
    blueHex = blue.replace('0x','')

    if (int(r) < 16):
        redFinal=("0")+redHex.upper()
    else:
        redFinal = redHex.upper()

    if (int(g) < 16):
        greenFinal=("0")+greenHex.upper()

    else:
        greenFinal = greenHex.upper()


    if (int(b) < 16):
        blueFinal=("0")+blueHex.upper()

    else:
        blueFinal = blueHex.upper()

    valueHex = redFinal+greenFinal+blueFinal
    return ("#")+valueHex

def menu():
    print("\n1. Load Colour File \n2. Print All colours \n3. Select Colour\n"+
        "4. Find Closest Colour \n5. Display(Save) Colour Scheme \n0. Quit \n")



dict ={}


menu()

num =int(input("Select an option:  ").strip())

while (num != 0):


    # take the numbers between 1-5 only
    if (num>5 or num<0):

        print("Your input {} is invalid.".format(num))
        num =int(input("Select an option:  ").strip())


    if (num == 1):
        file=open("colours.csv")
        accColours = 0


        for line in file:

            linelist = line.split(",")
            rgbvalue = (int(linelist[1]),int(linelist[2]),int(linelist[3]))

            if rgbvalue not in dict.keys():
                accColours += 1

                # convert decim to hexadecimal
                colname = linelist [0]

                dict [rgbvalue]= colname, hexNumbers(int(linelist[1]),int(linelist[2]),int(linelist[3]))

        print("The file has been processed and",accColours,"colours were entered into the dictionary")

        file.seek(0)

        menu()
        num =int(input("Select an option:  ").strip())



    if(num == 2):

        print("Colour Name".ljust(12),"Red".ljust(3),"Green".ljust(5),"Blue".ljust(3),"Hex")
        print("-----------".ljust(12),"---".ljust(3),"-----".ljust(5),"----".ljust(3),"---")

        for key, values in dict.items():
            print(str(values[0]).ljust(12),str(key[0]).ljust(3),str(key[1]).ljust(5),str(key[2]).ljust(3),values[1])


        menu()
        num =int(input("Select an option:  ").strip())



    if(num == 3):
        print("Enter the RGB values of your color")

        userRed = int(input("R:"))
        userGreen =int(input("G:"))
        userBlue = int(input("B:"))

        hexNum = hexNumbers(userRed,userGreen,userBlue)
        userList = [int(userRed),int(userGreen),int(userBlue)]
        userTup=(int(userRed),int(userGreen),int(userBlue))

        if userTup in dict.keys():
            print("\nColour",userList,"is", dict[userTup][0],"and has hex code",dict[userTup][1])

        else:
            notFound=int(input("\nColour "+str(userList)+" was not found. Would you like: \n1. Enter a name for this colour \
                \n2. Return to the main menu \nSelect an option:    "))

            if notFound == 1:
                newCol=input("What is the color name?  ")
                newHex=hexNumbers(userRed,userGreen,userBlue)
                dict[userTup]= newCol,str(newHex)
                print("Colour "+str(userList)+" is "+str(newCol)+" and has hex code "+str(newHex))

            elif notFound == 2:
                print("Return to the menu")

        menu()

        num =int(input("Select an option:  ").strip())


    if (num == 4):

        minDiff=750

        print("Enter the RGB values of your color")

        userRed = int(input("R:"))
        userGreen =int(input("G:"))
        userBlue = int(input("B:"))

        hexNum = hexNumbers(userRed,userGreen,userBlue)
        userList = [int(userRed),int(userGreen),int(userBlue)]
        userTup=(int(userRed),int(userGreen),int(userBlue))

        if userTup in dict.keys():
            print("\nColour",userList,"is", dict[userTup][0],"and has hex code",dict[userTup][1])

        else:
            for key, value in dict.items():
                diff= abs(userRed-key[0])+abs(userGreen-key[1])+abs(userBlue-key[2])
                if diff <= minDiff:
                    minDiff= diff
                    clList=[key[0],key[1],key[2]]
                    clName=value[0]
                    clHex=value[1]
            print("\nThe closet colour to "+str(userList)+" is " +str(clList)+", "+clName+", with hex code"+clHex)
            print("The absolute difference between the two colours is "+ str(minDiff))


        menu()
        num =int(input("Select an option:  ").strip())


    if (num == 5 ):

        print("Enter the RGB values of your color")

        userRed = int(input("R:"))
        userGreen =int(input("G:"))
        userBlue = int(input("B:"))

        scheme=input("Which color scheme do you wish to display? \n\nM: Monochrome \nC: Complementary \n\nSelect an option:   ").lower().strip()

        while (scheme != "c" and scheme!= "m"):
            print("Your input {} is invalid. Enter M or C.".format(scheme))

            scheme=input("Which color scheme do you wish to displaye? \n\nM: Monochrome \nC: Complementary \n\nSelect an option: ").lower().strip()

        if scheme == "m":

            mono=cmpt120colours.square(userRed,userGreen,userBlue,240,240)

            cmpt120colours.monochrome(mono,userRed,userGreen,userBlue,0)

            cmpt120image.showImage(mono)
            cmpt120image.saveImage(mono,"Monochrome.png")

        if scheme == "c":

            comp=cmpt120colours.square(userRed,userGreen,userBlue,480,240)

            compRed = 255 - userRed
            compGreen=255 - userGreen
            compBlue = 255 -userBlue

            for row in range(240,480):
                for col in range(240):
                    comp[col][row]=[compRed,compGreen,compBlue]

            cmpt120colours.monochrome(comp,userRed,userGreen,userBlue,0)
            cmpt120colours.complimentary(comp,compRed,compGreen,compBlue,240)

            cmpt120image.showImage(comp)
            cmpt120image.saveImage(comp,"Complementary.png")

        menu()
        num =int(input("Select an option:   ").strip())

if num == 0:
    print("Bye")
