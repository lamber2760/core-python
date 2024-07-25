def cm_to_feet(feet):
    return feet /30
n = int(input("Enter the value in cms :"))
print(f"The corresponding value is cms { cm_to_feet(round(n))}")