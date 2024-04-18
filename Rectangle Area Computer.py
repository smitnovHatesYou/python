print("So you'd like to find the area of a rectangle? I can solve it for you! (Give me all of your measurments in centimeters please!)")

length = input("So first, what's the lenght of your rectangle?:  ")

print(length)

width = input("Second, what's the width of your trangle?:  ")

print(width)

print("The equation we will be using is A = L * W. This means that the area is equal to the length multiplied by the width.")

area = int(length) * int(width)

print("The area of your rectangle is " + str(area) + " centimeters squared.")