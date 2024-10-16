import streamlit as st

def calculate_tax(income, tax_rate):
    """Calculate tax based on income and tax rate."""
    return income * (tax_rate / 100)

# Streamlit App UI
st.title("Tax Calculator")

# Input income
income = st.number_input("Enter your total income:", min_value=0.0, step=1000.0)

# Tax brackets and rates
tax_brackets = {
    "Low Income (0-40,000)": 10,
    "Middle Income (40,001-100,000)": 20,
    "High Income (100,001-200,000)": 30,
    "Very High Income (200,001 and above)": 35
}

# Determine applicable tax rate
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

# Display results when button is pressed
if st.button("Calculate Tax"):
    st.write(f"Your income: ${income:.2f}")
    st.write(f"Applicable tax rate: {tax_rate}%")
    st.write(f"Total tax owed: ${tax_owed:.2f}")
