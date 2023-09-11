from time import time


def timeActive(startTime):
    '''
    Prints how long the claw program has been active.

    Parameters
    ----------
    startTime : Time when program started
    
    Returns
    -------
    None.
    '''
    timeNow=time()
    activeTime=timeNow-startTime
    print("Program was active for", activeTime, "seconds.")


def listAverage(positionList, sumList):
    '''
    This function will print the average claw position as percent.
    
    Parameters
    ----------
    positionList : List of claw position samples taken every loop of main
    code block.
    sumList : The sum of the samples taken every loop of main
    code block.

    Returns
    -------
    None.

    '''
    clawAverage = sumList/len(positionList) # calculate average.
    print("Average claw position is", clawAverage, "percent.") # print average.
