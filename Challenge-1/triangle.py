side_1 = int(input("Enter the side 1:"))
side_2 = int(input("Enter the side 2:"))
side_3 = int(input("Enter the side 3:"))    

if side_1 == side_2 == side_3:
    print("Equilateral Triangle")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")