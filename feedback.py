from engi1020.arduino import digital_read, analog_read, digital_write


def checkButtonOne(buttonPin):
    '''
    Checks the state of button one
    
    Parameters
    ----------
    buttonPin : Pin that button is plugged into.
    
    Returns
    -------
    bool; True if button pressed, False if not pressed.
    '''
    if digital_read(buttonPin)==1:
        return True
    else:
        return False


def warning(grabDialPin, ledPin):
    '''
    If the claw is closed (grabber dial is close to end), LED will turn on to 
    let the user know.

    Parameters
    ----------
    grabDialPin : Pin number that grabber dial is plugged into.
    ledPin : Pin number that LED is plugged into.

    Returns
    -------
    None.

    '''
    checkDial = analog_read(grabDialPin) 
    if checkDial > 950:
        digital_write(ledPin,1)
    else: 
        digital_write(ledPin,0)