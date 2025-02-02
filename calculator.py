import streamlit as st

def calculate_old_tax(salary):
    if salary <= 700000:
        return 0

    tax = 0
    remaining = salary

    slabs = [
        (300000, 0.00),
        (100000, 0.05),
        (600000, 0.10),
        (200000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]

    for slab, rate in slabs:
        if remaining > 0:
            taxable_amount = min(remaining, slab)
            tax += taxable_amount * rate
            remaining -= taxable_amount
    
    return tax

def calculate_new_tax(salary):
    if salary <= 1200000:
        return 0

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
            taxable_amount = min(remaining, slab)
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
                color: #bdc3c7;
                text-align: center;
            }
            .highlight-old {
                font-size: 1.2rem;
                font-weight: bold;
                color: #2563EB;
            }
            
            .highlight-new {
                 font-size: 1.2rem;
                font-weight: bold;
                color: #16A34A;
            }
                
            .result-box-old {
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

salary = st.number_input("## Enter Annual Income (₹)", min_value=0, step=10000, format="%d")

if salary > 0:
    old_tax = calculate_old_tax(salary)
    new_tax = calculate_new_tax(salary)
    
    old_effective_rate = (old_tax / salary) * 100
    new_effective_rate = (new_tax / salary) * 100
    
    st.markdown("<h2 class='sub-title'>Old Tax Calculation as per 2024</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box-old'>{format_currency(old_tax)}</div>", unsafe_allow_html=True)
    st.markdown(f"<p class='highlight-old'>Effective Rate: {old_effective_rate:.1f}%</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='sub-title'>New Tax Calculation as per 2025 Budget</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box-new'>{format_currency(new_tax)}</div>", unsafe_allow_html=True)
    st.markdown(f"<p class='highlight-new'>Effective Rate: {new_effective_rate:.1f}%</p>", unsafe_allow_html=True)

    # Display all percentage slabs
    st.markdown("## Tax Slabs & Rates")
    st.markdown("### Old Tax Regime")
    old_slabs = [
        ("0 - 3L", "0%"),
        ("3L - 4L", "5%"),
        ("4L - 10L", "10%"),
        ("10L - 12L", "15%"),
        ("12L - 15L", "20%"),
        ("Above 15L", "30%")
    ]
    
    for slab, rate in old_slabs:
        st.markdown(f"**{slab}** : {rate}")
    
    st.markdown("### New Tax Regime")
    new_slabs = [
        ("0 - 4L", "0%"),
        ("4L - 8L", "5%"),
        ("8L - 12L", "10%"),
        ("12L - 16L", "15%"),
        ("16L - 20L", "20%"),
        ("20L - 24L", "25%"),
        ("Above 24L", "30%")
    ]
    
    for slab, rate in new_slabs:
        st.markdown(f"**{slab}** : {rate}")