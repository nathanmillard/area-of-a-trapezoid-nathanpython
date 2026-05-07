print("Let's calculate the area of a trapezoid")

# Get user inputs
base_a = float(input("How long should the bottom be? "))
base_b = float(input("How long should the top be? "))
height = float(input("How tall should it be? "))

# Calculate the area
area = ((base_a + base_b) / 2) * height

# Display the results
print(f"The area is, with a bottom length of {base_a} cm, a top length of {base_b} cm, and a height of {height} cm, gives us an area of {area} cm^2")
