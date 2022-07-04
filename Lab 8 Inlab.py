
# Define the function for calculating the income tax
def calculate_income_tax():
    # Initialize the constants
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000
    DEPENDENT_DEDUCTION = 3000

    # Take the inputs
    gross_income = float(input("Enter your gross income: "))
    num_dependents = int(input("Enter the number of your dependents: "))

    # Compute the income tax
    taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dependents
    income_tax = taxable_income * TAX_RATE

    # Display the income tax
    print("Your income tax is $" + str(income_tax))

# Define the main function
def main():
    calculate_income_tax()

# Execution point of the program
if __name__ == "__main__":
    main()