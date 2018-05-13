name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#Conversions
#1 inch = 2.54cm
height_cm = height * 2.54

#1 pound = 0.45 kg
weight_kg = weight * 0.453592

print(f"He's height in cm is {round(height_cm)} cm's")
print(f"He's weight in kg is {round(weight_kg)} kg's")
