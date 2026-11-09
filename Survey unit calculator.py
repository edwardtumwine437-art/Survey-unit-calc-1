
import math


def convert_length():
    print("\n--- LENGTH CONVERSION ---")
    print("1. Metres to kilometres")
    print("2. Kilometres to metres")
    print("3. Metres to centimetres")
    print("4. Metres to millimetres")
    print("5. Metres to feet")
    print("6. Feet to metres")
    print("7. Metres to yards")

    choice = input("Choose conversion (1-7): ")
    value = float(input("Enter the measurement: "))

    conversions = {
        "1": ("kilometres", value / 1000),
        "2": ("metres", value * 1000),
        "3": ("centimetres", value * 100),
        "4": ("millimetres", value * 1000),
        "5": ("feet", value * 3.280839895),
        "6": ("metres", value / 3.280839895),
        "7": ("yards", value * 1.093613298)
    }

    if choice in conversions:
        unit, result = conversions[choice]
        print(f"Result: {result:.4f} {unit}")
    else:
        print("Invalid conversion choice.")


def convert_area():
    print("\n--- AREA CONVERSION ---")
    print("1. Hectares to square metres")
    print("2. Square metres to hectares")
    print("3. Hectares to acres")
    print("4. Acres to hectares")

    choice = input("Choose conversion (1-4): ")
    value = float(input("Enter the area: "))

    conversions = {
        "1": ("square metres", value * 10000),
        "2": ("hectares", value / 10000),
        "3": ("acres", value * 2.4710538147),
        "4": ("hectares", value / 2.4710538147)
    }

    if choice in conversions:
        unit, result = conversions[choice]
        print(f"Result: {result:.4f} {unit}")
    else:
        print("Invalid conversion choice.")


def convert_angle():
    print("\n--- ANGLE CONVERSION ---")
    print("1. Degrees to radians")
    print("2. Radians to degrees")

    choice = input("Choose conversion (1-2): ")
    value = float(input("Enter the angle: "))

    if choice == "1":
        print(f"Result: {math.radians(value):.6f} radians")
    elif choice == "2":
        print(f"Result: {math.degrees(value):.4f} degrees")
    else:
        print("Invalid conversion choice.")


def calculate_distance():
    print("\n--- DISTANCE BETWEEN SURVEY POINTS ---")
    x1 = float(input("Enter Easting of point 1: "))
    y1 = float(input("Enter Northing of point 1: "))
    x2 = float(input("Enter Easting of point 2: "))
    y2 = float(input("Enter Northing of point 2: "))

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Horizontal distance: {distance:.3f} metres")


def calculate_rectangle_area():
    print("\n--- RECTANGULAR PLOT AREA ---")
    length = float(input("Enter length in metres: "))
    width = float(input("Enter width in metres: "))

    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
        return

    area = length * width
    print(f"Area: {area:.3f} square metres")
    print(f"Area: {area / 10000:.4f} hectares")


def main():
    while True:
        print("\n================================")
        print(" SURVEY MEASUREMENT CALCULATOR")
        print("================================")
        print("1. Length conversion")
        print("2. Area conversion")
        print("3. Angle conversion")
        print("4. Distance between survey points")
        print("5. Calculate rectangular plot area")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                convert_length()
            elif choice == "2":
                convert_area()
            elif choice == "3":
                convert_angle()
            elif choice == "4":
                calculate_distance()
            elif choice == "5":
                calculate_rectangle_area()
            elif choice == "6":
                print("Thank you for using the calculator.")
                break
            else:
                print("Invalid choice. Select a number from 1 to 6.")

        except ValueError:
            print("Error: Enter a valid number.")
        except OverflowError:
            print("Error: The value is too large to calculate.")


if __name__ == "__main__":
    main()
