import streamlit as st
import matplotlib.pyplot as plt

# Streamlit app
st.title("🏡 Mortgage Affordability Calculator")

# User inputs
st.header("Enter Your Financial Details")
income = st.number_input("Monthly Income ($):", min_value=500, value=5000, step=100)
expenses = st.number_input("Monthly Expenses ($):", min_value=0, value=2000, step=100)
down_payment = st.number_input("Down Payment ($):", min_value=0, value=20000, step=1000)
loan_term = st.slider("Loan Term (years):", 5, 30, 15)
interest_rate = st.slider("Interest Rate (%):", 1.0, 10.0, 4.0)

# Constants
DTI_RATIO = 0.36  # Safe debt-to-income ratio
MONTHS_IN_YEAR = 12

# Calculations
max_monthly_mortgage = (income - expenses) * DTI_RATIO
max_loan_amount = (
    max_monthly_mortgage
    * (1 - (1 + (interest_rate / 100 / MONTHS_IN_YEAR)) ** (-loan_term * MONTHS_IN_YEAR))
) / (interest_rate / 100 / MONTHS_IN_YEAR)
affordable_home_price = max_loan_amount + down_payment

# Display results
st.header("Affordability Results")
st.write(f"💰 Maximum Affordable Home Price: **${affordable_home_price:,.2f}**")
st.write(f"📅 Maximum Monthly Mortgage Payment: **${max_monthly_mortgage:,.2f}**")

# Visualization
st.header("Income Distribution")
labels = ["Mortgage", "Expenses", "Remaining Income"]
sizes = [max_monthly_mortgage, expenses, income - expenses - max_monthly_mortgage]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
st.pyplot(fig)

# Tips
st.header("💡 Savings Tips")
if max_monthly_mortgage < expenses:
    st.write("⚠️ Your expenses are too high compared to your income. Consider reducing unnecessary expenses.")
if down_payment < 0.2 * affordable_home_price:
    st.write("💡 Aim for a down payment of at least 20% to avoid private mortgage insurance (PMI).")


