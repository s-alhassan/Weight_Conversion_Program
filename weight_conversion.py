print("***Weight Conversion Program***")

while True:
    try:
        weight = float(input("Enter the weight: "))
        if weight >= 0:
            unit = input("Enter the weight unit [kg / lb]: ").lower()
            if unit == "kg":
                lb = weight * 2.20462
                print(f"{weight} in kg is equal to {lb:.2f} in lbs.")
                print("*******************************")

            elif unit == "lb":
                kg = weight * 0.453592
                print(f"{weight} in lbs is equal to {kg:.2f} in kg.")
                print("*******************************")

            else:
                print(f"{unit} is not a valid weight unit. Please enter either 'kg' or 'lb'.")
                print("**************END**************") 
        else:
            print("Please Enter a positive number")     
    except(ValueError):
        print("It is not a valid input please enter a number.")
        print("*******************************")

    choice = input("Would you like to convert another weight? [y / n]: ").lower()
    if choice != "y":
        break
print("Thank you, see you soon!!")