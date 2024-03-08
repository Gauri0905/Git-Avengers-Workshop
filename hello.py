import numpy as np
def classify_traingle(a,b,c):
     sides = np.array([a, b, c])
     if any(side <= 0 for side in sides) or np.max(sides) >= np.sum(sides) - np.max(sides):
         return "Not a valid triangle"
     if np.allclose(sides, sides[0]):
         return "Equilateral triangle"
     elif len(set(sides)) == 2:
         return "Isosceles triangle"
     elif any(np.isclose(sides**2, np.roll(sides, -1)**2 + np.roll(sides, -2)**2)):
         return "Right-angled triangle"
     else:
         return "Scalene triangle"
s1= float(input("Enter 1st side"))
s2= float(input("Enter 2nd side"))
s3= float(input("Enter 3rd side"))
result= classify_traingle(s1,s2,s3)
print(result)
