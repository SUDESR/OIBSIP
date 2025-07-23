def calculate_bmi(weight, height):
    """Calculate the BMI using the its formula: weight (kg) / height² (m²)"""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Classify the BMI into categories based on standard WHO ranges"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator")

    try:
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
