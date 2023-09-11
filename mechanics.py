from engi1020.arduino import analog_read, servo_move, lcd_clear, lcd_print, lcd_hsv


def grab(grabDialPin, grabServoPin):
    '''
    Changes grabbing servo angle based on primary dial position
    
    Parameters
    ----------
    grabDialPin : Pin that dial to control grabbing servo is plugged into
    grabServoPin : Pin that grabbing servo is plugged into
    
    Returns
    -------
    None.
    '''
    dialOne=analog_read(grabDialPin)/341*60 #Converts dial position to something the servo can use
    servo_move(grabServoPin, dialOne) #Changes servo position based on dial


def pivot(pivotDialPin, pivotServoPin):
    '''
    Changes pivoting servo angle based on secondary dial position. 
    Prints position of pivoting arm as a percent and changes the backlight 
    color based on position as well. Screen will turn red at either end of 
    the pivot.
    
    Parameters
    ----------
    pivotDialPin : Pin that dial to control pivoting servo is plugged into
    pivotServoPin : Pin that pivoting servo is plugged into
    
    Returns
    -------
    None.
    '''
    dialTwo=analog_read(pivotDialPin)/341*60
    servo_move(pivotServoPin, dialTwo)
    lcd_clear()
    lcd_print(dialTwo/1.8)
    colorIndicator=analog_read(pivotDialPin)/1023
    lcd_hsv(colorIndicator,0.6,100)
