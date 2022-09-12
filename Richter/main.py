def joules(richter):
    return 10**((1.5*richter)+4.8)
def tnt(richter):
    return joules(richter)/(4.184*10**9)
def print_predefined_values():
    print(f"""
{"Richter":<24}{"Joules":<24}{"TNT":<24}
{1:<24}{joules(1):<24}{tnt(1):<30}
{5:<24}{joules(5):<24}{tnt(5):<30}
{9.1:<24}{joules(9.1):<24}{tnt(9.1):<30}
{9.2:<24}{joules(9.2):<24}{tnt(9.2):<30}
{9.5:<24}{joules(9.5):<24}{tnt(9.5):<30}
""")
def user_input():
    return float(input(f"Please enter a richter scale value: "))
def print_output(richter):
    print(f"""
Richter value: {richter}
Equivalence in joules: {joules(richter)}
Equivalence in tons of TNT: {tnt(richter)}
""")
print_predefined_values()
print_output(user_input())

