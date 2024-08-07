from bmi_calculator.calculations import calculate_bmi, bmi_category

def main():
    """
    Main function to run the BMI calculator.
    """
    print("Welcome to the BMI Calculator!")
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    if isinstance(bmi, str):
        print(bmi)
    else:
        category = bmi_category(bmi)
        print(f"Your BMI is {bmi}. You are categorized as: {category}")

if __name__ == "__main__":
    main()
