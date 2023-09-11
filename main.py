from engi1020.arduino import lcd_hsv, analog_read
from time import time

from feedback import check_button_one, warning
from mechanics import grab, pivot
from utils import list_avg, time_active


def main():
    
    print("Welcome to claw program.")
    print('---') #Print some break lines so console is more organized

    grab_dial_pin = int(input("What analog pin is the grabber dial plugged into? "))
    grab_servo_pin = int(input("What digital pin is the grabber servo plugged into? "))
    pivot_dial_pin = int(input("What analog pin is the pivot dial plugged into? "))
    pivot_servo_pin = int(input("What digital pin is the pivot servo plugged into? "))
    button_pin = int(input("What digital pin is the button plugged into? "))
    led_pin = int(input("What digital pin is the LED plugged into? "))
    print('---')

    lcd_hsv(0.5,0.5,100) #Initialize LCD Settings (Hue, Saturation, Brightness).
    position_list = [] #Create list for claw position samples.
    sum_list=0 #Create variable for sum of claw position samples so average can be calculated later.
    claw_position = analog_read(grab_dial_pin)/10.23 #Convert grabber dial value to a percent value.

    print("Claw program is now active.")
    print('---')
    start_time = time() #Record time of code start point for later use.

    while True: #Open loop so claw positions and user info can be continually changed.
        #grab(grab_dial_pin, grab_servo_pin)
        pivot(pivot_dial_pin, pivot_servo_pin)
        warning(grab_dial_pin, led_pin)
        position_list.append(claw_position) #Add percent claw position to list of samples.
        sum_list += claw_position #Add percent claw position to the sum variable
        if check_button_one(button_pin) == True: #Loop will end when button is pressed, ending the program.
            break

    list_avg(position_list, sum_list) #Prints average claw position.
    time_active(start_time) #Prints amount of time that claw was active, in seconds.
    print("Thank you for using claw program.")


if __name__ == "__main__":
    main()
