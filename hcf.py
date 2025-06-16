def hcf(valuelist):
    divisor = min(valuelist)
    while not all([v % divisor == 0 for v in valuelist]):
        divisor -= 1
    return divisor

print("HCF PROGRAM")
print("\nTYPE THE NUMBERS YOU WANT, LEAVE BLANK TO CALCULATE")
x = ""
values = []
entering=True
while entering:
    x = input("?: ")
    if x.lower() != "":
        x = int(x)
        values.append(x)
    else:
        entering = False
print(f"HCF of {values} is {hcf(values)}")
        
