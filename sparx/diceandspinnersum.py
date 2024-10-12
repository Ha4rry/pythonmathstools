numerator=0
denominator=0
dice_sides=6
spinner_numbers = [1,3,6]
less_than_num = 5
for i in range(1,dice_sides+1):
    for o in spinner_numbers:
        if i+o<less_than_num:
            numerator+=1
        denominator+=1
print(numerator)
print("---")
print(denominator)
