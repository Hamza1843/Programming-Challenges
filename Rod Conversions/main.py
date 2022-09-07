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

def user_input():
    global rods
    rods = float(input("Input rods: "))
def print_conversions():
    print(f"""
You input {rods} rods.

Conversions
Meters: {meters(rods)}
Feet: {feet(rods)}
Furlongs: {furlongs(rods)}
Minutes to walk 10.0 rods: {time_to_walk(rods)}""")

if __name__ == '__main__':
    user_input()
    print_conversions()