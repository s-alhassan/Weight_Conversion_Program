# Weight_Conversion_Program
# Weight Conversion Program

A simple Python command-line application that converts weights between **kilograms (kg)** and **pounds (lb)**. The program validates user input, handles common errors, and allows users to perform multiple conversions until they choose to exit.

## Features

* Convert **kilograms (kg)** to **pounds (lb)**.
* Convert **pounds (lb)** to **kilograms (kg)**.
* Prevents negative weight values.
* Handles non-numeric input using exception handling.
* Validates weight units (`kg` or `lb`).
* Lets users perform multiple conversions in one session.
* Displays converted values rounded to two decimal places.

## How It Works

1. Enter a weight.
2. Select the weight unit (`kg` or `lb`).
3. The program calculates and displays the converted weight.
4. Choose whether to perform another conversion.
5. Enter **`y`** to continue or **`n`** to exit the program.

## Example Output

```text
***Weight Conversion Program***

Enter the weight: 75
Enter the weight unit [kg / lb]: kg
75.0 in kg is equal to 165.35 in lbs.

Would you like to convert another weight? [y / n]: n
Thank you, see you soon!!
```

## Technologies Used

* Python 3
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Exception handling (`try` / `except`)
* User input and formatted output
