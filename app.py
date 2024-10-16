import streamlit as st
import math

# Scientific Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def square_root(x):
    return math.sqrt(x)

def exponent(x, y):
    return x ** y

def logarithm(x, base=math.e):
    if x > 0:
        return math.log(x, base)
    else:
        return "Logarithm undefined for non-positive values!"

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Streamlit App UI
st.title("Scientific Calculator")

# Choose the operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", 
                                              "Square Root", "Exponent", "Logarithm", 
                                              "Sine", "Cosine", "Tangent"])

# Input numbers
if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponent"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

# Input for single number functions
if operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]:
    num1 = st.number_input("Enter a number", value=0.0)

# Handle operation
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)
elif operation == "Square Root":
    result = square_root(num1)
elif operation == "Exponent":
    result = exponent(num1, num2)
elif operation == "Logarithm":
    base = st.number_input("Enter base for logarithm (default is e)", value=math.e)
    result = logarithm(num1, base)
elif operation == "Sine":
    result = sine(num1)
elif operation == "Cosine":
    result = cosine(num1)
elif operation == "Tangent":
    result = tangent(num1)

# Display the result
if st.button("Calculate"):
    st.write(f"Result: {result}")
