from engi1020.arduino import analog_read, servo_move, lcd_clear, lcd_print, lcd_hsv


def grab(grab_dial_pin, grab_servo_pin):
    '''
    Changes grabbing servo angle based on primary dial position
    
    Parameters
    ----------
    grab_dial_pin : Pin that dial to control grabbing servo is plugged into
    grab_servo_pin : Pin that grabbing servo is plugged into
    
    Returns
    -------
    None.
    '''
    dial_one=analog_read(grab_dial_pin)/341*60 #Converts dial position to something the servo can use
    servo_move(grab_servo_pin, dial_one) #Changes servo position based on dial


def pivot(pivot_dial_pin, pivot_servo_pin):
    '''
    Changes pivoting servo angle based on secondary dial position. 
    Prints position of pivoting arm as a percent and changes the backlight 
    color based on position as well. Screen will turn red at either end of 
    the pivot.
    
    Parameters
    ----------
    pivot_dial_pin : Pin that dial to control pivoting servo is plugged into
    pivot_servo_pin : Pin that pivoting servo is plugged into
    
    Returns
    -------
    None.
    '''
    dial_two=analog_read(pivot_dial_pin)/341*60
    servo_move(pivot_servo_pin, dial_two)
    lcd_clear()
    lcd_print(dial_two/1.8)
    color_indicator=analog_read(pivot_dial_pin)/1023
    lcd_hsv(color_indicator,0.6,100)
