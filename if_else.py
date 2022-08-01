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
print("Done")