from math import floor, ceil, log, pi

def decifloor(num, deci=0): #floor function where rounding place can be specified
    if deci == 0:
        return floor(num)
    
    elif deci != 0:
        return (floor(num * pow(10, deci)) / pow(10, deci))
    
def deciceil(num, deci=0): #ceiling function where rounding place can be specified
    if deci == 0:
        return ceil(num)
    
    elif deci != 0:
        return (ceil(num * pow(10, deci)) / pow(10, deci))

def clamp(num, lower, upper): #limit number to range
    if num < lower:
        num = lower
    elif num > upper:
        num = upper
    return num

def lerp(first, second, step): #linearly interpolate between two values, CURRENTLY UNTESTED
    self.difference = second - first
    return first + (self.difference * step)

def Map(x, in_min, in_max, out_min, out_max): #map one range to another
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def log(base, arg): #log with variable base
    return log(arg)/log(base)

def radians(degrees): #currently untested
    return degrees * (pi / 180)

def degrees(radians): #currently untested
    return radians * (180 / pi)