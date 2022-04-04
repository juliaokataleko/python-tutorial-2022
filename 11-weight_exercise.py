from lib2to3.pytree import convert


weight = int(input("Weight: "))

unity = input("(K)g or (L)bs")

if unity.upper() == "L":
    converted = weight / 0.45
    print("Weight in pound is: ", converted)
else:
    converted = weight * 0.45
    print("Weight in Kg is: ", converted)
