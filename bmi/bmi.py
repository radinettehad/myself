
def input_user_data():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi  
def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
def main():
    weight, height = input_user_data()
    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}") 


main()