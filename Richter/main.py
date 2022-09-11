def joules(richter):
    return 10**((1.5*richter)+4.8)
def tnt(energy):
    return energy/(4.184*10**9)
def print_predefined_values():
    print(f"""
Richter                 Joules                  TNT
1                       {joules(1)}      {tnt(joules(1))}
5                       {joules(5)}      {tnt(joules(5))}
9.1                     {joules(9.1)}   {tnt(joules(9.1))}
9.2                     {joules(9.2)}   {tnt(joules(9.2))}
9.5                     {joules(9.5)}  {tnt(joules(9.5))}
""")
def user_input():
    global richter
    richter = float(input(f"Please enter a richter scale value: "))
def print_output():
    print(f"""
Richter value: {richter}
Equivalence in joules: {joules(richter)}
Equivalence in tons of TNT: {joules(richter)}
""")

