import math

def taxicab_circle_y(r):
    point_set = set()
    y = 0
    for angle in range(360):
        theta = math.radians(angle)
        x = int(r*math.sin(theta))
        z = int(r*math.cos(theta))
        if (x,y, z) not in point_set:
            point_set.add((x, y, z))
    return point_set

def taxicab_filled_y(r_max):

    point_set = set()
    for r in range(r_max):
        y = 0
        for angle in range(360):
            theta = math.radians(angle)
            x = r*math.sin(theta)
            z = r*math.cos(theta)
            if (x,y, z) not in point_set:
                point_set.add((x, y, z))
    return point_set

def taxicab_circle_x(r):
    point_set = set()
    x = 0
    for angle in range(360):
        theta = math.radians(angle)
        y = r*math.sin(theta)
        z = r*math.cos(theta)
        if (x,y, z) not in point_set:
            point_set.add((x, y, z))
    return point_set

def taxicab_circle_z(r):
    point_set = set()
    z = 0
    for angle in range(360):
        theta = math.radians(angle)
        x = r*math.sin(theta)
        y = r*math.cos(theta)
        if (x,y, z) not in point_set:
            point_set.add((x, y, z))
    return point_set