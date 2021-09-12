from flask import Flask
app = Flask(__name__)

@app.route("/")
def area():
  a_t = input(f"Enter the shape name(Square/Triangle/Rectangle/Parallelogram/Rhombus/Sphere/Cone): ")
  if a_t == "Square":
    D_E = int(input(f"Enter the side length: "))
    area = (D_E)**2
    print(area)
  elif a_t == "Rectangle":
    D_E = int(input(f"Enter the length: "))
    breadth = int(input(f"Enter the breadth: "))
    area = D_E*breadth
    print(area)
  elif a_t == "Triangle":
    D_E = int(input(f"Enter the base: "))
    BASE = int(input(f"Enter the height: "))
    area = (1/2)*(BASE)*(D_E)
    print(area)
  elif a_t == "Parallelogram":
    D_E = int(input("Enter the length of one side: "))
    HEIGHT = int(input("Enter the height: "))
    area = D_E*HEIGHT
    print(area)
  elif a_t == "Rhombus":
    D_E = int(input("Enter the first diagonal: "))
    diagonal = int(input("Enter the second diagonal: "))
    area = 1/2*(D_E*diagonal)
    print(area)
  elif a_t == "Trapezium":
    D_E = int(input("Enter the first base: "))
    base = int(input("Enter the second base: "))
    h_t = int(input("Enter the height: "))
    area = ((D_E+base)/2)*h_t
    print(area)
  elif a_t == "Circle":
    D_E = int(input("Enter the radius: "))
    area = 3.414*(D_E)**2
  elif a_t == "Cylinder":
    A=int(("Enter the radius of the base: "))
    ht = int(input("Enter the height: "))
    AREA_a = 2*3.414*A*ht
    print(" Curved Surface Area:" + str(AREA_a))
    AREA_b = 2*3.414*A*ht
    print("Total Surface Area:" + str(AREA_b))
  elif a_t == "Sphere":
    R=int(input("Enter the radius:"))
    AREA = 4*3.414*R**2
    print("Area of sphere is:" + str(AREA))
  elif a_t == "Right Circular Cone":
    R = int(input("Enter the radius of the base:"))
    h = int(input("Enter the height:"))
    CSA = 3.414*R*(R**2+h**2)**(1/2)
    TSA = 3.414*R*(R+(R**2+h**2)**(1/2))
    print("Curved Surface Area:" + str(CSA))
    print("Total Surface Area:" + str(TSA))
while True:
  area()
  contin = ""
  if contin not in ["no", "n", "yes", "y"]:
    contin = input(f"Do you wish to enter another calculation? (Yes/No): ")
    if contin.lower() in ["no", "n"]:
      break
    elif contin.lower() in ["yes", "y"]:
      continue

