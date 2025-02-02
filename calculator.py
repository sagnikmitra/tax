import streamlit as st

def calculate_pre_budget_new_regime_tax(salary):
    if salary <= 775000:
        return 0

    standard_deduction = 75000
    tax = 0
    remaining = salary

    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]

    for slab, rate in slabs:
        if remaining > 0:
            taxable_amount = min(remaining, slab) - standard_deduction
            tax += taxable_amount * rate
            remaining -= taxable_amount
    
    return tax

def calculate_pre_budget_old_regime_tax(salary):
    if salary <= 500000:
        return 0

    standard_deduction = 50000
    tax = 0
    remaining = salary

    slabs = [
        (250000, 0.00),
        (250000, 0.05),
        (500000, 0.20),
        (float('inf'), 0.30)
    ]

    for slab, rate in slabs:
        if remaining > 0:
            taxable_amount = min(remaining, slab) - standard_deduction
            tax += taxable_amount * rate
            remaining -= taxable_amount
    
    return tax

def calculate_post_budget_new_tax(salary):
    if salary <= 1275000:
        return 0

    standard_deduction = 75000
    tax = 0
    remaining = salary

    slabs = [
        (400000, 0.00),
        (400000, 0.05),
        (400000, 0.10),
        (400000, 0.15),
        (400000, 0.20),
        (400000, 0.25),
        (float('inf'), 0.30)
    ]

    for slab, rate in slabs:
        if remaining > 0:
            taxable_amount = min(remaining, slab) - standard_deduction
            tax += taxable_amount * rate
            remaining -= taxable_amount
    
    return tax

def format_currency(amount):
    return f'₹{amount:,.0f}'

# Set up branding
def set_branding():
    st.markdown("""
        <style>
            body {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            .main-title {
                font-size: 2.5rem;
                font-weight: bold;
                color: #ecf0f1;
                text-align: center;
            }
            .sub-title {
                font-size: 1.5rem;
                color: white;
                text-align: center;
            }
            .highlight-pre-old {
                font-size: 1.2rem;
                font-weight: bold;
                color: #ffcc00;
            }
            
            .highlight-pre-new {
                font-size: 1.2rem;
                font-weight: bold;
                color: #2563EB;
            }

            .highlight-new {
                 font-size: 1.2rem;
                font-weight: bold;
                color: #16A34A;
            }
                
            .result-box-pre-old {
                background-color: #ffffc5;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 1.3rem;
                font-weight: bold;
                color: #ba8e23;
            }
            
            .result-box-pre-new {
                background-color: #EFF6FF;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 1.3rem;
                font-weight: bold;
                color: #2563EB;
            }

            .result-box-new {
                background-color: #F0FDF4;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 1.3rem;
                font-weight: bold;
                color: #16A34A;
            }
            
            .old-regime {
                background-color: #2980b9;
                padding: 10px;
                border-radius: 5px;
                color: #ecf0f1;
            }
            .new-regime {
                background-color: #27ae60;
                padding: 10px;
                border-radius: 5px;
                color: #ecf0f1;
            }
        </style>
    """, unsafe_allow_html=True)

st.title("💰 Tax Calculator Comparison as per Budget 2025")

st.write("### by Sagnik Mitra")
set_branding()

if "salary" not in st.session_state:
    st.session_state.salary = 0

# Update session state only after the button is clicked
temp_salary = st.number_input("## Enter Annual Income Below (₹)", step=10000, min_value=0, format="%d")

if st.button("Calculate"):
    st.session_state.salary = temp_salary  # Store value only when button is clicked

# Use session state for salary
salary = st.session_state.salary

if salary > 0:
    pre_budget_new_regime_tax = calculate_pre_budget_new_regime_tax(salary)
    pre_budget_old_regime_tax = calculate_pre_budget_old_regime_tax(salary)
    post_budget_new_tax = calculate_post_budget_new_tax(salary)
    
    pre_budget_new_regime_effective_rate = (pre_budget_new_regime_tax / salary) * 100
    pre_budget_old_regime_effective_rate = (pre_budget_old_regime_tax / salary) * 100
    post_budget_new_effective_rate = (post_budget_new_tax / salary) * 100
    
    st.markdown("<h2 class='sub-title'>Pre-Budget Old Regime Tax Calculation as per 2024</h2>", unsafe_allow_html=True)
    pre_budget_old_regime_tax_post_cess = pre_budget_old_regime_tax*1.04
    st.markdown(f"<div class='result-box-pre-old'>{format_currency(pre_budget_old_regime_tax_post_cess)}</div>", unsafe_allow_html=True)
    st.warning("Shown tax includes 4 percent CESS")
    pre_budget_old_regime_tax_in_hand_per_month_salary = int((salary - pre_budget_old_regime_tax_post_cess)/12)
    st.markdown(f"<p class='highlight-pre-old'>Effective Rate: {pre_budget_old_regime_effective_rate:.1f}%<br>In-Hand Per Month Salary: {pre_budget_old_regime_tax_in_hand_per_month_salary}</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='sub-title'>Pre-Budget New Regime Tax Calculation as per 2024</h2>", unsafe_allow_html=True)
    pre_budget_new_regime_tax_post_cess = pre_budget_new_regime_tax*1.04
    st.markdown(f"<div class='result-box-pre-new'>{format_currency(pre_budget_new_regime_tax_post_cess)}</div>", unsafe_allow_html=True)
    st.info("Shown tax includes 4 percent CESS")
    pre_budget_new_regime_tax_in_hand_per_month_salary = int((salary - pre_budget_new_regime_tax_post_cess)/12)
    st.markdown(f"<p class='highlight-pre-new'>Effective Rate: {pre_budget_new_regime_effective_rate:.1f}%<br>In-Hand Per Month Salary: {pre_budget_new_regime_tax_in_hand_per_month_salary}</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='sub-title'>Post Budget New Tax Calculation as per 2025</h2>", unsafe_allow_html=True)
    post_budget_new_tax_post_cess = post_budget_new_tax*1.04
    st.markdown(f"<div class='result-box-new'>{format_currency(post_budget_new_tax_post_cess)}</div>", unsafe_allow_html=True)
    st.success("Shown tax includes 4 percent CESS")
    post_budget_new_tax_in_hand_per_month_salary = int((salary - post_budget_new_tax_post_cess)/12)
    st.markdown(f"<p class='highlight-new'>Effective Rate: {post_budget_new_effective_rate:.1f}%<br>In-Hand Per Month Salary: {post_budget_new_tax_in_hand_per_month_salary}</p>", unsafe_allow_html=True)

    total_savings_pre_budget_new_and_post_budget = pre_budget_new_regime_tax_post_cess - post_budget_new_tax_post_cess
    st.info(f"### Total Savings if you were in New Regime before Budget: {format_currency(total_savings_pre_budget_new_and_post_budget)}")

    total_savings_pre_budget_old_and_post_budget = pre_budget_old_regime_tax_post_cess - post_budget_new_tax_post_cess
    st.warning(f"### Total Savings if you were in Old Regime before Budget: {format_currency(total_savings_pre_budget_old_and_post_budget)}")
    
    # Display all percentage slabs
    st.markdown("## Tax Slabs & Rates")
    st.markdown("### Pre Budget Old Tax Regime")
    new_slabs = [
        ("0 - 2.5L", "0%"),
        ("2.5L - 5L", "5%"),
        ("5L - 10L", "20%"),
        ("Above 24L", "30%")
    ]
    
    for slab, rate in new_slabs:
        st.markdown(f"**{slab}** : {rate}")
    st.markdown("### Pre Budget New Tax Regime")
    old_slabs = [
        ("0 - 3L", "0%"),
        ("3L - 6L", "5%"),
        ("6L - 9L", "10%"),
        ("9L - 12L", "15%"),
        ("12L - 15L", "20%"),
        ("Above 15L", "30%")
    ]
    
    for slab, rate in old_slabs:
        st.markdown(f"**{slab}** : {rate}")

    st.markdown("### Post Budget New Tax Regime")
    old_slabs = [
        ("0 - 4L", "0%"),
        ("4L - 8L", "5%"),
        ("8L - 12L", "10%"),
        ("12L - 16L", "15%"),
        ("16L - 20L", "20%"),
        ("20L - 24L", "25%"),
        ("Above 24L", "30%")
    ]
    
    for slab, rate in old_slabs:
        st.markdown(f"**{slab}** : {rate}")
    
    
