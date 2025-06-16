def every_item_can_be_divided_into(ls,dividend):
    divisible = True
    for item in ls:
        if dividend % item != 0:
            divisible = False
            break
    return divisible

def lcm(valuelist):
    dividend = max(valuelist)
    while not every_item_can_be_divided_into(valuelist,dividend):
        dividend+=1
    return dividend
print("LCM PROGRAM")
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
print(f"LCM of {values} is {lcm(values)}")
