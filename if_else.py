temperature = 12

if temperature > 30:
    print("It's a hot day")
    print("Drink more water")
elif temperature > 20: #(20, 30]
    print("It's a nice day")
elif temperature > 10: #(10, 20]
    print("It's a cold day")
else:
    print("It's cold")

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs:" + str(converted))
print("Done")