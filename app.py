import streamlit as st
import pandas as pd

# Page Title and Introduction
st.title("💼 HR Operation Calculator")
st.subheader("What is HR Software?", divider=True)
st.write("HR software helps manage human resources tasks like hiring, payroll, performance tracking, and more. It streamlines operations and improves productivity.")

st.subheader("What Does This Calculator Do?", divider=True)
st.write("""
This calculator estimates how much HR automation can reduce HR staffing needs and salary costs based on your industry and company size.

A key factor in this calculation is **productivity gain** — the expected improvement in efficiency when routine HR tasks are automated.  
For example, if automation improves productivity by 30%, your company may require fewer HR staff to manage the same number of employees, resulting in cost savings.
""")

# Input Section
st.header("🚀 Let's Try It Out!")
st.caption("Please enter your company data below:")

# User Inputs
total_emp = st.number_input("👥 Total number of employees", min_value=2, value=500)
avg_hr_salary = st.number_input("💰 Average monthly HR salary (THB)", min_value=10000, value=35000)
industry = st.selectbox("🏭 Select your industry", [
    'general', 'leisure and hospitality', 'transport and utilities',
    'manufacturing', 'construction', 'health', 'education',
    'finance and insurance', 'business service', 'information', 'other services'
    ],
    help="Different industries have varying HR needs. Sectors with stringent regulatory requirements, like healthcare and finance, may need a higher HR-to-employee ratio to maintain compliance."
    )

st.caption("Industry HR-to-employee ratios are based on data from [HiBob – HR to Employee Ratio](https://www.hibob.com/hr-glossary/hr-to-employee-ratio/)")

st.info("""
**Adjusting Productivity Gain**

Use the slider below to estimate how much efficiency improves with HR automation.

- A **higher percentage** reflects greater improvements (e.g., automating repetitive admin tasks).
- A **lower percentage** reflects modest changes (e.g., partial digitalization).

💡 If you're unsure, a **30% productivity gain** is a typical estimate for companies starting to adopt HR automation.
""")


productivity_gain = st.slider("⚙️ Productivity gain from HR automation (%)", 0.0, 1.0, 0.3, 0.05)

# HR staff per 100 employees by industry
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

# Button to show results
if st.button("Calculate Results"):
    # HR ratio
    emp_per_hr = 100 / hr_per_emp[industry]

    # HR Calculation
    total_hr = max(1, round(total_emp / emp_per_hr))
    cost_before = total_hr * avg_hr_salary

    total_hr_after = round(total_hr / (1 + productivity_gain))
    cost_after = total_hr_after * avg_hr_salary
    cost_saving = cost_before - cost_after
    reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100 if total_hr else 0

    # Display Results as Table
    st.subheader("📊 Results Summary")

    results_data = {
        " ": ["HR Needed", "Monthly Cost (THB)"],
        "Before Automation": [total_hr, f"{cost_before:,.0f}"],
        "After Automation": [total_hr_after, f"{cost_after:,.0f}"]
    }

    results_df = pd.DataFrame(results_data)
    results_df.set_index(" ", inplace=True)  # Set first column as index
    st.table(results_df)

    st.write(f"**HR reduction:** {reduction_percent:.1f}%")

    # Summary Metric
    st.metric(label="🎉 Monthly Savings", value=f"{cost_saving:,.0f} THB")

    # Bar Chart
    cost_diff = pd.DataFrame({
        "Before": [cost_before],
        "After": [cost_after]
    })

    melted = pd.melt(cost_diff, var_name="Stage", value_name="Cost (THB/month)")
    melted["Stage"] = pd.Categorical(melted["Stage"], categories=["Before", "After"], ordered=True)
    melted = melted.sort_values("Stage")

    st.bar_chart(melted, x="Stage", y="Cost (THB/month)")

    # Explanation of Benefits
    st.subheader("🔍 What This Means for You")
    st.markdown("""
    By adopting HR automation, your organization can:
    
    - **Reduce HR workload and staffing needs** by automating repetitive administrative tasks, improving efficiency.
    - **Enhance the employee experience**, strengthen compliance, and accelerate processes.
    - **Achieve greater HR cost-efficiency and save on monthly salary costs.**
    - **Gain valuable data insights and increase scalability for growth.**
    - **Improve data accuracy and reduce errors.**
    - **Free up the HR team for strategic work.**
  
    💡 These improvements help modernize HR practices while supporting business growth.
    """)