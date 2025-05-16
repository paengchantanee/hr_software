import streamlit as st
import pandas as pd

st.title("HR Operation")
st.write("Calculate the number of HR headquarter and the cost before and after using HR automation")

# Inputs
total_emp = st.number_input("Total employees", min_value=2, value=500)
avg_hr_salary = st.number_input("Average HR salary (THB/month)", min_value=10000, value=35000)
industry = st.selectbox("Industry", [
    'general', 'leisure and hospitality','transport and utilities',
    'manufacturing', 'construction','health', 'education',
    'finance and insurance','business service', 'information','other services'
])

# Number of HR staff per 100 employees by industry
hr_per_emp = {
    'general': 1,
    'leisure and hospitality': 1.91,
    'transport and utilities': 1.96,
    'manufacturing': 2.29,
    'construction': 2.38,
    'health': 2.71,
    'education': 2.78,
    'finance and insurance': 2.85,
    'business service': 2.92,
    'information': 2.97,
    'other services': 3.62
}
# HR ratio
emp_per_hr = 100 / hr_per_emp[industry]

# (Adjustable) Productivity gain with HR automation
productivity_gain = st.slider("Productivity gain from automation (%)", 0.0, 1.0, 0.3, 0.05)

# HR Calculation
# Before
total_hr = max(1, round(total_emp / emp_per_hr))
cost_before = total_hr * avg_hr_salary
# After
total_hr_after = round(total_hr / (1 + productivity_gain))
cost_after = total_hr_after * avg_hr_salary
cost_saving = cost_before - cost_after
reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100 if total_hr else 0

# Display
st.subheader("Results")
st.write(f"**HR needed:** {total_hr}")
st.write(f"**Cost before automation:** {cost_before:,.0f} THB/month")
st.write("---")
st.write(f"**HR after automation:** {total_hr_after}")
st.write(f"**HR reduced:** {reduction_percent:.1f}%")
st.write(f"**Cost after automation:** {cost_after:,.0f} THB/month")

# Metric summary
st.metric(label="Cost Saved", value=f"{cost_saving:,.0f} THB/month")

# Bar Chart
cost_diff = pd.DataFrame({
    "Before" : [cost_before],
    "After" : [cost_after]
})

melted = pd.melt(cost_diff, var_name="Stage", value_name="Cost THB/month")
melted["Stage"] = pd.Categorical(melted["Stage"], categories=["Before", "After"], ordered=True)
melted = melted.sort_values("Stage")

st.bar_chart(melted, x="Stage", y="Cost THB/month")
