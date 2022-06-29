'''
# CostonP1
# Programmer: John Coston
# Email: jcoston@cnm.edu
# Purpose: demonstrate use of functions using A distance calculator. Calculate distance between two latitude and longitude points
# Created on Jun 24, 2022
'''
#Imports
from pip._vendor.distlib.compat import raw_input
import math
#variables
#Header Function to write purpose and header
def writeHeader():
    print('Welcome to distance calculator today we will\n'\
          'Calculate distance between two latitude and longitude points.')
#Get Location from user and return tuple or list
def getLocation():
    correctInput = False
    lat = ()
    long = ()
    while correctInput == False:
        lat = float(input('Please enter the latitude coordinate/n'/
        'positive for northern hemisphere negative for southern hemisphere: '))
        if lat >= -90 and lat <= 90:
            correctInput = True
        else:
            print('\nError: please enter a number between 90 and -90')
    while correctInput == True:
        long = float(input('Please enter the Longitude coordinate/n'/
        'Positive for easter hemisphere negative for western hemisphere: '))
        if long >= -180 and long <= 180:
            break
        else:
            print('\nError: please enter a number between 180 and -180')
    return lat,long
#Distance calculator
def calculateDistance(origin,destination):
    radius = 6371000  # radius of Earth in meters
    #subtract the latitude and longitude and convert to radians
    '''
    Haversine formula located here: https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
    '''
    lat1, lon1 = origin
    lat2, lon2 = destination
    #Convert to radians for equation to work.
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)    
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1) 
    #Calculate distance using the Haversine Formula   
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    meters = radius * c  # output distance in meters    
    km = meters / 1000.0  # output distance in kilometers
    meters = round(meters, 3)
    km = round(km, 3)       
    #I think this is the equation from the promt
    return km
#Goodbye Message
def goodBye():
    print('Thank you for using distance calculator goodbye!')
#call Header
writeHeader()
#Do another loop
doAnother = 'y'
while doAnother == 'y':
    #Call Get location
    firstPoint = getLocation()
    #add spacer and explain a second location is required
    print('\nNext please enter the second location bellow\n')    
    #Call getLocation Again
    SecondPoint = getLocation()
    #Call Distance
    distance = calculateDistance(firstPoint,SecondPoint)
    #print data
    print('The distance between {} and {} is approximately {:.3f} kilometers.'.format(firstPoint,SecondPoint,distance))
    #Ask Do another
    doAnother = raw_input('Again y/n: ').strip().lower()[0]
goodBye()
