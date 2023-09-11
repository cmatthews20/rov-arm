from engi1020.arduino import digital_read, analog_read, digital_write


def check_button_one(button_pin):
    """
    Checks the state of button one

    Parameters
    ----------
    button_pin : Pin that button is plugged into.

    Returns
    -------
    bool; True if button pressed, False if not pressed.
    """
    if digital_read(button_pin) == 1:
        return True
    else:
        return False


def warning(grab_dial_pin, led_pin):
    """
    If the claw is closed (grabber dial is close to end), LED will turn on to
    let the user know.

    Parameters
    ----------
    grab_dial_pin : Pin number that grabber dial is plugged into.
    led_pin : Pin number that LED is plugged into.

    Returns
    -------
    None.

    """
    check_dial = analog_read(grab_dial_pin)
    if check_dial > 950:
        digital_write(led_pin, 1)
    else:
        digital_write(led_pin, 0)
