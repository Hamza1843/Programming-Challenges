def meters(rods):
    return(rods*5.0292)
def feet(rods):
    return(meters(rods)/0.3048)
def miles(rods):
    return(meters(rods)/1609.34)
def furlongs(rods):
    return(rods/40)
def time_to_walk(rods):
    return(miles(rods)/3.1*60)
