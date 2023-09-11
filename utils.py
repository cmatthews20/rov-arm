from time import time


def time_active(start_time):
    """
    Prints how long the claw program has been active.

    Parameters
    ----------
    start_time : Time when program started

    Returns
    -------
    None.
    """
    time_now = time()
    active_time = time_now - start_time
    print("Program was active for", active_time, "seconds.")


def list_avg(position_list, sum_list):
    """
    This function will print the average claw position as percent.

    Parameters
    ----------
    position_list : List of claw position samples taken every loop of main
    code block.
    sum_list : The sum of the samples taken every loop of main
    code block.

    Returns
    -------
    None.

    """
    claw_avg = sum_list / len(position_list)  # calculate average.
    print("Average claw position is", claw_avg, "percent.")  # print average.
