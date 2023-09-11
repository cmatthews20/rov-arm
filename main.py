from engi1020.arduino import lcd_hsv, analog_read
from time import time

from feedback import checkButtonOne, warning
from mechanics import grab, pivot
from utils import listAverage, timeActive


def main():
    
    print("Welcome to claw program.")
    print('---') #Print some break lines so console is more organized

    grabDialPin = int(input("What analog pin is the grabber dial plugged into? "))
    grabServoPin = int(input("What digital pin is the grabber servo plugged into? "))
    pivotDialPin = int(input("What analog pin is the pivot dial plugged into? "))
    pivotServoPin = int(input("What digital pin is the pivot servo plugged into? "))
    buttonPin = int(input("What digital pin is the button plugged into? "))
    ledPin = int(input("What digital pin is the LED plugged into? "))
    print('---')

    lcd_hsv(0.5,0.5,100) #Initialize LCD Settings (Hue, Saturation, Brightness).
    positionList = [] #Create list for claw position samples.
    sumList=0 #Create variable for sum of claw position samples so average can be calculated later.
    clawPosition = analog_read(grabDialPin)/10.23 #Convert grabber dial value to a percent value.

    print("Claw program is now active.")
    print('---')
    startTime = time() #Record time of code start point for later use.

    while True: #Open loop so claw positions and user info can be continually changed.
        #grab(grabDialPin, grabServoPin)
        pivot(pivotDialPin, pivotServoPin)
        warning(grabDialPin, ledPin)
        positionList.append(clawPosition) #Add percent claw position to list of samples.
        sumList += clawPosition #Add percent claw position to the sum variable
        if checkButtonOne(buttonPin) == True: #Loop will end when button is pressed, ending the program.
            break

    listAverage(positionList, sumList) #Prints average claw position.
    timeActive(startTime) #Prints amount of time that claw was active, in seconds.
    print("Thank you for using claw program.")


if __name__ == "__main__":
    main()
