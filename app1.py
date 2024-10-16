# Tax Calculator in Google Colab

def calculate_tax(income, tax_rate):
    """Calculate tax based on income and tax rate."""
    return income * (tax_rate / 100)

def tax_calculator():
    print("Welcome to the Tax Calculator!")

    # Input income
    income = float(input("Enter your total income: $"))

    # Tax brackets (example rates)
    tax_brackets = {
        "Low Income (0-40,000)": 10,
        "Middle Income (40,001-100,000)": 20,
        "High Income (100,001-200,000)": 30,
        "Very High Income (200,001 and above)": 35
    }

    # Display tax brackets and rates
    print("\nTax Brackets:")
    for bracket, rate in tax_brackets.items():
        print(f"{bracket}: {rate}%")

    # Select applicable tax bracket
    if income <= 40000:
        tax_rate = tax_brackets["Low Income (0-40,000)"]
    elif income <= 100000:
        tax_rate = tax_brackets["Middle Income (40,001-100,000)"]
    elif income <= 200000:
        tax_rate = tax_brackets["High Income (100,001-200,000)"]
    else:
        tax_rate = tax_brackets["Very High Income (200,001 and above)"]

    # Calculate tax
    tax_owed = calculate_tax(income, tax_rate)

    # Display results
    print(f"\nYour income: ${income:.2f}")
    print(f"Applicable tax rate: {tax_rate}%")
    print(f"Total tax owed: ${tax_owed:.2f}")

# Run the tax calculator
tax_calculator()
