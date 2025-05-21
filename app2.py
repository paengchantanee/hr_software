import streamlit as st
import pandas as pd

# Language selector
language = st.selectbox("🌐 Select Language / เลือกภาษา", ["English", "ภาษาไทย"])

# Text dictionaries
texts = {
    "English": {
        "title": "💼 HR Operation Calculator",
        "intro1": "What is HR Software?",
        "intro1_body": "HR software helps manage human resources tasks like hiring, payroll, performance tracking, and more. It streamlines operations and improves productivity.",
        "intro2": "What Does This Calculator Do?",
        "intro2_body": """
This calculator estimates how much HR automation can reduce HR staffing needs and salary costs based on your industry and company size.

A key factor in this calculation is **productivity gain** — the expected improvement in efficiency when routine HR tasks are automated.

For example, if automation improves productivity by 30%, your company may require fewer HR staff to manage the same number of employees, resulting in cost savings.
""",
        "section_header": "🚀 Let's Try It Out!",
        "input_caption": "Please enter your company data below:",
        "total_emp": "👥 Total number of employees",
        "avg_salary": "💰 Average monthly HR salary (THB)",
        "industry": "🏭 Select your industry",
        "industry_names": [
            'general', 'leisure and hospitality', 'transport and utilities',
            'manufacturing', 'construction', 'health', 'education',
            'finance and insurance', 'business service', 'information', 'other services'
        ],
        "help": "Different industries have varying HR needs. Sectors with stringent regulatory requirements, like healthcare and finance, may need a higher HR-to-employee ratio to maintain compliance.",
        "productivity_help": """
**Adjusting Productivity Gain**

Use the slider below to estimate how much efficiency improves with HR automation.

- A **higher percentage** reflects greater improvements.
- A **lower percentage** reflects modest changes.

💡 If you're unsure, a **30% productivity gain** is a typical estimate for companies starting to adopt HR automation.
""",
        "slider_label": "⚙️ Productivity gain from HR automation (%)",
        "button": "Calculate Results",
        "result_header": "📊 Results Summary",
        "before": "Before Automation",
        "after": "After Automation",
        "row_hr": "HR Needed",
        "row_cost": "Monthly Cost (THB)",
        "reduction": "HR reduction",
        "savings_monthly": "🎉 Monthly Savings",
        "savings_yearly": "💰 Yearly Savings",
        "savings_percent": "📈 Cost Savings (%)",
        "explain_header": "🔍 What This Means for You",
        "explain_body": """
By adopting HR automation, your organization can:

- **Reduce HR workload** and staffing needs by automating administrative tasks.
- **Enhance the employee experience**, compliance, and process speed.
- **Achieve HR cost-efficiency and save on salary costs.**
- **Gain insights and scale easily.**
- **Improve accuracy and reduce errors.**
- **Free HR for strategic work.**

💡 These improvements help modernize HR practices while supporting growth.
""",
        "source_caption": "📘 source: Industry HR-to-employee ratios are based on data from [HiBob – HR to Employee Ratio](https://www.hibob.com/hr-glossary/hr-to-employee-ratio/)"
    },
    "ภาษาไทย": {
        "title": "💼 เครื่องคำนวณฝ่ายทรัพยากรบุคคล",
        "intro1": "ซอฟต์แวร์ HR คืออะไร?",
        "intro1_body": "ซอฟต์แวร์ HR ช่วยจัดการงานต่าง ๆ ของฝ่ายทรัพยากรบุคคล เช่น การสรรหาบุคลากร การจ่ายเงินเดือน การติดตามผลการปฏิบัติงาน และอื่น ๆ ซึ่งช่วยให้การดำเนินงานมีประสิทธิภาพมากขึ้น",
        "intro2": "เครื่องคำนวณนี้ทำอะไรได้บ้าง?",
        "intro2_body": """
เครื่องคำนวณนี้ช่วยประมาณจำนวนพนักงานฝ่าย HR และคำนวณค่าใช้จ่ายรายเดือน ก่อนและหลังจากการนำระบบอัตโนมัติมาใช้ในฝ่าย HR

ปัจจัยสำคัญในการคำนวณนี้คือ **อัตราการเพิ่มประสิทธิภาพ (Productivity Gain)** ซึ่งหมายถึงการปรับปรุงประสิทธิภาพที่คาดว่าจะเกิดขึ้นเมื่อมีการนำระบบอัตโนมัติมาใช้กับงาน HR

เช่น หากระบบช่วยเพิ่มประสิทธิภาพ 30% บริษัทอาจต้องการพนักงาน HR น้อยลง ส่งผลให้ประหยัดค่าใช้จ่าย
""",
        "section_header": "🚀 มาลองใช้กันเลย!",
        "input_caption": "กรุณากรอกข้อมูลของบริษัทของคุณ:",
        "total_emp": "👥 จำนวนพนักงานทั้งหมด",
        "avg_salary": "💰 เงินเดือนเฉลี่ยของ HR ต่อเดือน (บาท)",
        "industry": "🏭 เลือกประเภทอุตสาหกรรมของคุณ",
        "industry_names": [
            'ทั่วไป', 'นันทนาการและการโรงแรม', 'ขนส่งและสาธารณูปโภค',
            'การผลิต', 'ก่อสร้าง', 'สุขภาพ', 'การศึกษา',
            'การเงินและประกันภัย', 'บริการ', 'เทคโนโลยีสารสนเทศ', 'บริการอื่น ๆ'
        ],
        "help": "อุตสาหกรรมต่าง ๆ มีความต้องการด้านทรัพยากรบุคคลที่แตกต่างกัน ภาคส่วนที่มีข้อกำหนดด้านกฎระเบียบที่เข้มงวด เช่น การแพทย์และการเงิน อาจจำเป็นต้องมีอัตราส่วนบุคลากร HR ต่อพนักงานที่สูงกว่าเพื่อให้เป็นไปตามข้อกำหนด",
        "productivity_help": """
**การปรับค่าอัตราการเพิ่มประสิทธิภาพ (Productivity Gain)**

ใช้แถบเลื่อนด้านล่างเพื่อประมาณการว่าประสิทธิภาพจะเพิ่มขึ้นมากน้อยเพียงใดเมื่อนำระบบซอฟต์แวร์ HR มาใช้

- **เปอร์เซ็นต์ที่สูงขึ้น** หมายถึงการปรับปรุงประสิทธิภาพที่มากขึ้น
- **เปอร์เซ็นต์ที่ต่ำลง** หมายถึงการเปลี่ยนแปลงที่ไม่มาก

💡 หากไม่แน่ใจ ค่า **30%** เป็นค่าประมาณทั่วไปสำหรับบริษัทที่เริ่มต้นนำระบบซอฟต์แวร์ HR มาใช้งาน
""",
        "slider_label": "⚙️ อัตราการเพิ่มประสิทธิภาพจากการใช้ซอฟต์แวร์ HR (%)",
        "button": "คำนวณผลลัพธ์",
        "result_header": "📊 สรุปผลลัพธ์",
        "before": "ก่อนใช้ระบบ",
        "after": "หลังใช้ระบบ",
        "row_hr": "จำนวน HR ที่ต้องใช้",
        "row_cost": "ค่าใช้จ่ายรายเดือน (บาท)",
        "reduction": "จำนวน HR ที่ลดลง",
        "savings_monthly": "🎉 เงินที่ประหยัดได้ต่อเดือน",
        "savings_yearly": "💰 เงินที่ประหยัดได้ต่อปี",
        "savings_percent": "📈 อัตราการประหยัดค่าใช้จ่าย (%)",
        "explain_header": "🔍 สิ่งนี้มีความหมายต่อองค์กรของคุณอย่างไร",
        "explain_body": """
การนำระบบ HR อัตโนมัติมาใช้ องค์กรของคุณจะได้รับประโยชน์ดังนี้:

- **ลดภาระงาน** และความต้องการของบุคลากร HR โดยการให้ระบบอัตโนมัติทำงานบริหารจัดการแทน
- **ยกระดับการทำงานของพนักงาน** และความรวดเร็วของกระบวนการ
- **จัดสรรต้นทุนได้ง่ายขึ้น** และประหยัดค่าใช้จ่ายต่าง ๆ เช่น เงินเดือน ค่าถ่ายเอกสาร เป็นต้น
- **ได้รับข้อมูลเชิงลึก** และนำไปขยายขนาดองค์กรให้ดีขึ้น
- **ให้บุคลากร HR มีเวลามากขึ้นสำหรับงานเชิงกลยุทธ์**

💡 การปรับปรุงเหล่านี้ช่วยให้การดำเนินงาน HR ทันสมัยและสนับสนุนการเติบโตขององค์กร
""",
        "source_caption": "📘 แหล่งข้อมูล: อัตราส่วน HR ต่อพนักงานในแต่ละอุตสาหกรรม อ้างอิงจากข้อมูลของ [HiBob – HR to Employee Ratio](https://www.hibob.com/hr-glossary/hr-to-employee-ratio/)"
    }
}

t = texts[language]

# Industry keys for calculation
industry_keys = [
    'general', 'leisure and hospitality', 'transport and utilities',
    'manufacturing', 'construction', 'health', 'education',
    'finance and insurance', 'business service', 'information', 'other services'
]

# UI
st.title(t["title"])
st.subheader(t["intro1"], divider=True)
st.write(t["intro1_body"])
st.subheader(t["intro2"], divider=True)
st.write(t["intro2_body"])

st.header(t["section_header"])
st.caption(t["input_caption"])

# Inputs
total_emp = st.number_input(t["total_emp"], min_value=2, value=500)
avg_hr_salary = st.number_input(t["avg_salary"], min_value=10000, value=35000)

# Industry selectbox
industry_display = st.selectbox(
    label=f"{t['industry']}",
    options=t["industry_names"],
    help=t["help"]
)
industry = industry_keys[t["industry_names"].index(industry_display)]

# Adjustable productivity gain
st.info(t["productivity_help"])
productivity_gain = st.slider(t["slider_label"], 0.0, 1.0, 0.3, 0.05)

# HR ratio
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

# Button & Calculation
if st.button(t["button"]):
    emp_per_hr = 100 / hr_per_emp[industry]
    # Before automation
    total_hr = max(1, round(total_emp / emp_per_hr))
    cost_before = total_hr * avg_hr_salary
    # After automation
    total_hr_after = round(total_hr / (1 + productivity_gain))
    cost_after = total_hr_after * avg_hr_salary
    cost_saving_monthly = cost_before - cost_after
    cost_saving_yearly = cost_saving_monthly * 12
    savings_percent = (cost_saving_monthly / cost_before) * 100 if cost_before > 0 else 0
    reduction_percent = ((total_hr - total_hr_after) / total_hr) * 100 if total_hr else 0

    # Result table
    st.subheader(t["result_header"])
    results_df = pd.DataFrame({
        " ": [t["row_hr"], t["row_cost"]],
        t["before"]: [total_hr, f"{cost_before:,.0f}"],
        t["after"]: [total_hr_after, f"{cost_after:,.0f}"]
    })
    results_df.set_index(" ", inplace=True)
    st.table(results_df)

    st.write(f"**{t['reduction']}:** {reduction_percent:.1f}%")
    st.metric(label=t["savings_monthly"], value=f"{cost_saving_monthly:,.0f} THB")
    st.metric(label=t["savings_yearly"], value=f"{cost_saving_yearly:,.0f} THB")
    st.metric(label=t["savings_percent"], value=f"{savings_percent:.1f}%")

    # Bar chart
    cost_diff = pd.DataFrame({"Before": [cost_before], "After": [cost_after]})
    melted = pd.melt(cost_diff, var_name="Stage", value_name="Cost (THB/month)")
    melted["Stage"] = pd.Categorical(melted["Stage"], categories=["Before", "After"], ordered=True)
    melted = melted.sort_values("Stage")
    st.bar_chart(melted, x="Stage", y="Cost (THB/month)")

    # Explanation of Benefit
    st.subheader(t["explain_header"])
    st.markdown(t["explain_body"])

# Source
st.caption(t["source_caption"])
