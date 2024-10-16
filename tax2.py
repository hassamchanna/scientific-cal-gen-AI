import streamlit as st

def calculate_tax(income, tax_rate):
    """Calculate tax based on income and tax rate."""
    return income * (tax_rate / 100)

# Streamlit App UI
st.title("Tax Calculator")

# Input currency selection
currency = st.selectbox("Select Currency:", ["Pakistani Rupees (PKR)", "US Dollars (USD)"])

# Input income
income = st.number_input(f"Enter your total income in {currency}:", min_value=0.0, step=1000.0)

# Define tax rates based on the selected currency
if currency == "Pakistani Rupees (PKR)":
    tax_brackets = {
        "Low Income (0-1,000,000 PKR)": 10,
        "Middle Income (1,000,001-2,500,000 PKR)": 20,
        "High Income (2,500,001-5,000,000 PKR)": 30,
        "Very High Income (5,000,001 PKR and above)": 35
    }
elif currency == "US Dollars (USD)":
    tax_brackets = {
        "Low Income (0-40,000 USD)": 10,
        "Middle Income (40,001-100,000 USD)": 20,
        "High Income (100,001-200,000 USD)": 30,
        "Very High Income (200,001 USD and above)": 35
    }

# Determine applicable tax rate
if income <= (1000000 if currency == "Pakistani Rupees (PKR)" else 40000):
    tax_rate = tax_brackets["Low Income (0-1,000,000 PKR)" if currency == "Pakistani Rupees (PKR)" else "Low Income (0-40,000 USD)"]
elif income <= (2500000 if currency == "Pakistani Rupees (PKR)" else 100000):
    tax_rate = tax_brackets["Middle Income (1,000,001-2,500,000 PKR)" if currency == "Pakistani Rupees (PKR)" else "Middle Income (40,001-100,000 USD)"]
elif income <= (5000000 if currency == "Pakistani Rupees (PKR)" else 200000):
    tax_rate = tax_brackets["High Income (2,500,001-5,000,000 PKR)" if currency == "Pakistani Rupees (PKR)" else "High Income (100,001-200,000 USD)"]
else:
    tax_rate = tax_brackets["Very High Income (5,000,001 PKR and above)" if currency == "Pakistani Rupees (PKR)" else "Very High Income (200,001 USD and above)"]

# Calculate tax
tax_owed = calculate_tax(income, tax_rate)

# Display results when button is pressed
if st.button("Calculate Tax"):
    st.write(f"Your income: {income:.2f} {currency}")
    st.write(f"Applicable tax rate: {tax_rate}%")
    st.write(f"Total tax owed: {tax_owed:.2f} {currency}")
