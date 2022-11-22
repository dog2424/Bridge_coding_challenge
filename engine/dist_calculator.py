import math
from datetime import timedelta

# Setting of parameters used for approximated distance calculations
earth_radius = 6371.0000785
distance_factor = 1.24
average_speed = 77.2


def compute_airdist(point1, point2):
    """
   Function to compute the air distance between two points
   :param point1: object of type Point (to be written)
   :param point2: object of type Point (to be written)
   :return: distance as float in [meter or kilometer]
   """
    a = (math.sin(math.radians(point1.latitude - point2.latitude) / 2) ** 2 + math.cos(math.radians(point1.latitude))
         * math.cos(math.radians(point2.latitude))
         * (math.sin(math.radians(point1.longitude - point2.longitude) / 2)
             ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = earth_radius * c
    return d


def compute_dist_approach(point1, point2):
    """
    Function to compute an estimation for the distance to drive between two
    points.
    :param point1: object of type Point (to be written)
    :param point2: object of type Point (to be written)
    :return: distance as float in [meter or kilometer]
    """
    airdist = compute_airdist(point1, point2)
    return airdist * distance_factor


def compute_time_approach(point1, point2):
    """
    Function to compute an estimation for the time needed to drive the distance
    between two points.
    :param point1: object of type Point (to be written)
    :param point2: object of type Point (to be written)
    :return: time as timedelta
    """
    dist_approach = compute_dist_approach(point1, point2)
    if dist_approach < 100:
        average_speed = 30 + dist_approach * 0.472
    else:
        average_speed = average_speed
    timedelta_return = timedelta(hours=dist_approach / average_speed)
    return timedelta_return
