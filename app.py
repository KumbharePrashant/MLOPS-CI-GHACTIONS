import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter the number to calculate its square, cube and to the 5th power.")

# user input
n = st.number_input("Enter an integer", value=1,step=1)

# calculate results
square = n**2
cube = n**3
fifth_power = n**5

# Display results
st.write(f"Square of number {n} is {square}")
st.write(f"Cube of number {n} is {cube}")
st.write(f"Fifth power of number {n} is {fifth_power}")
