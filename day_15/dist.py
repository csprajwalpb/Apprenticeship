import math

point1 = (3, 4)
point2 = (7, 9)

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

print("\n" + "="*40)
print("    Distance Between Two Points ")
print("="*40)
print(f"Point 1 : {point1}")
print(f"Point 2 : {point2}")
print(f"Distance: {distance:.2f}")
print("="*40)
