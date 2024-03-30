from datetime import datetime
import time


# Part 1
def clock(n):
    """
    shows the time and updates it once every second for n seconds

    Parameters
    ------------
    n: int
        number of seconds to update clock for
    ------------

    Returns
    ------------
    none
    ------------
    """
    # Your code here
    time_format = "%Y-%m-%d %H:%M:%S.%f"
    for i in range(n):
        time_object = datetime.strptime(str(datetime.now()), time_format)
        print(f"{time_object.hour}:{time_object.minute}:{time_object.second}", end = "\r")
        time.sleep(1)

# Part 2
def lcm(a, b):
    """
    calculates the lowest common multiple of integers a and b

    Parameters
    ------------
    a: int
        first integer
    b: int
        second integer
    ------------

    Returns
    ------------
    int
    ------------
    """
    # Your code here
    a_original = a
    b_original = b
    while a != b:
        if a < b:
            a += a_original
        elif b < a:
            b += b_original
    lcm = a
    return(lcm)


# Part 3
def gcf(a, b):
    """
    calculates the greatest common factor of integers a and b

    Parameters
    ------------
    a: int
        first integer
    b: int
        second integer
    ------------

    Returns
    ------------
    int
    ------------
    """
    # Your code here
    while b != 0:
        r = a % b
        a = b
        b = r
    GCD = a
    return(GCD)