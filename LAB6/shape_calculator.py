import geometry_utils

operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")
operation = input("Enter the operation you want to perform: ")

if operation not in operations:
    print("Invalid operation!")
else:
    try:

        if "circle" in operation:
            r = float(input("Enter radius: "))
            result = operations[operation](r)

        elif "rectangle" in operation:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = operations[operation](w, h)

        elif "triangle" in operation:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = operations[operation](b, h)


        print(f"Result: {
        result:.2f}")

    except ValueError as error:

        if "could not convert" in str(error):
            print("Input Error: Lütfen sadece sayı giriniz.")
        else:
            print(f"Input Error: {error}")