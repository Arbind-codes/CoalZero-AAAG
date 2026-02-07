"""
CoalZero: Measuring Today, Planning Net-Zero
A decision-support tool for coal mining operations to measure carbon footprint
and plan pathways toward carbon neutrality
"""

import streamlit as st
import numpy as np
import pandas as pd

# Import calculation modules
from utils.emissions import (
    diesel_emissions,
    electricity_emissions,
    excavation_emissions,
    transportation_emissions,
    total_emissions,
    per_capita_emissions,
    emissions_in_tonnes
)

from utils.sinks import (
    total_absorption,
    absorption_in_tonnes,
    land_required_for_neutrality
)

from utils.simulations import (
    simulate_electrification,
    simulate_renewable_energy,
    simulate_afforestation,
    calculate_carbon_credits,
    combined_simulation
)

from visuals.plots import (
    emissions_vs_sinks_chart,
    activity_breakdown_chart,
    before_after_comparison,
    scenario_comparison_chart,
    gap_analysis_chart
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CoalZero - Carbon Neutrality Planner",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #27AE60;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #27AE60;
    }
    .warning-card {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #F39C12;
    }
    .success-card {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #27AE60;
    }
    .stButton>button {
        width: 100%;
        background-color: #27AE60;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown('<div class="main-header">🌱 CoalZero</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Measuring Today, Planning Net-Zero for Coal Mining Operations</div>', unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# SIDEBAR - USER INPUTS
# ==========================================

st.sidebar.header("📊 Operational Data Input")

st.sidebar.subheader("🔧 Mining Activities")

# Diesel consumption
diesel_litres = st.sidebar.number_input(
    "Diesel Consumption (litres/year)",
    min_value=0.0,
    value=50000.0,
    step=1000.0,
    help="Annual diesel consumption for excavation equipment"
)

# Electricity consumption
electricity_kwh = st.sidebar.number_input(
    "Electricity Consumption (kWh/year)",
    min_value=0.0,
    value=500000.0,
    step=10000.0,
    help="Annual electricity usage from grid"
)

# Coal excavation
coal_extracted = st.sidebar.number_input(
    "Coal Extracted (tonnes/year)",
    min_value=0.0,
    value=100000.0,
    step=5000.0,
    help="Annual coal extraction volume"
)

# Transportation
transport_distance = st.sidebar.number_input(
    "Average Transport Distance (km)",
    min_value=0.0,
    value=50.0,
    step=5.0,
    help="Average distance coal is transported"
)

# Workforce
num_workers = st.sidebar.number_input(
    "Number of Workers",
    min_value=1,
    value=500,
    step=10,
    help="Total workforce at the mine"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🌳 Existing Carbon Sinks")

# Plantation area
plantation_area = st.sidebar.number_input(
    "Plantation Area (hectares)",
    min_value=0.0,
    value=10.0,
    step=1.0,
    help="Current green cover / plantation area"
)

# Number of trees
num_trees = st.sidebar.number_input(
    "Additional Trees (count)",
    min_value=0,
    value=1000,
    step=100,
    help="Number of individual trees planted"
)


# ==========================================
# CALCULATIONS - CURRENT STATE
# ==========================================

# Calculate emissions
diesel_em = diesel_emissions(diesel_litres)
electricity_em = electricity_emissions(electricity_kwh)
excavation_em = excavation_emissions(coal_extracted)
transport_em = transportation_emissions(coal_extracted, transport_distance)

total_em = total_emissions(diesel_em, electricity_em, excavation_em, transport_em)
per_capita_em = per_capita_emissions(total_em, num_workers)

# Calculate sinks
total_absorption_kg = total_absorption(plantation_area, num_trees)

# Convert to tonnes
total_em_tonnes = emissions_in_tonnes(total_em)
total_absorption_tonnes = absorption_in_tonnes(total_absorption_kg)

# Gap analysis
emission_gap_kg = total_em - total_absorption_kg
emission_gap_tonnes = emission_gap_kg / 1000

# Land requirement
land_needed = land_required_for_neutrality(emission_gap_kg)


# ==========================================
# MAIN DASHBOARD - CURRENT STATUS
# ==========================================

st.header("📈 Current Carbon Footprint")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Emissions",
        value=f"{total_em_tonnes:.2f} tonnes/year",
        delta=None
    )

with col2:
    st.metric(
        label="Carbon Sinks",
        value=f"{total_absorption_tonnes:.2f} tonnes/year",
        delta=None
    )

with col3:
    st.metric(
        label="Emission Gap",
        value=f"{emission_gap_tonnes:.2f} tonnes/year",
        delta="Positive" if emission_gap_tonnes > 0 else "Neutral",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="Per Capita Emissions",
        value=f"{per_capita_em:.2f} kg/person/year",
        delta=None
    )

st.markdown("---")

# Display charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Emissions vs Sinks")
    fig1 = emissions_vs_sinks_chart(total_em_tonnes, total_absorption_tonnes)
    st.pyplot(fig1)

with col_right:
    st.subheader("🔍 Emission Sources")
    fig2 = activity_breakdown_chart(diesel_em, electricity_em, excavation_em, transport_em)
    st.pyplot(fig2)

st.markdown("---")

# Gap Analysis
st.subheader("⚖️ Gap Analysis")
fig_gap = gap_analysis_chart(total_em_tonnes, total_absorption_tonnes, emission_gap_tonnes)
st.pyplot(fig_gap)

# Check if all operational inputs are zero
all_inputs_zero = (diesel_litres == 0 and electricity_kwh == 0 and 
                   coal_extracted == 0 and transport_distance == 0)

if all_inputs_zero:
    st.info("ℹ️ **No Production Data Entered:** Your carbon production is currently 0. Please enter operational data in the sidebar to calculate emissions and carbon footprint.")
elif emission_gap_tonnes > 0:
    st.warning(f"⚠️ **Carbon Positive:** Your operation emits {emission_gap_tonnes:.2f} tonnes more CO₂ than it absorbs annually.")
    st.info(f"💡 **Land Requirement:** You would need approximately **{land_needed:.2f} hectares** of additional plantation to achieve carbon neutrality.")
else:
    st.success("✅ **Congratulations!** Your operation is carbon neutral or carbon negative.")

st.markdown("---")


# ==========================================
# SIMULATION SECTION
# ==========================================

st.header("🎯 Carbon Neutrality Pathways (Simulations)")

st.markdown("""
Explore **what-if scenarios** to see how different strategies can reduce your carbon footprint.
Adjust the sliders below to simulate emission reduction strategies.
""")

# Simulation inputs
st.subheader("🔧 Simulation Controls")

col_sim1, col_sim2, col_sim3 = st.columns(3)

with col_sim1:
    st.markdown("**🔋 Fleet Electrification**")
    electrification_pct = st.slider(
        "% of diesel vehicles electrified",
        min_value=0,
        max_value=100,
        value=30,
        step=5,
        help="Percentage of diesel-powered equipment replaced with electric alternatives"
    )

with col_sim2:
    st.markdown("**☀️ Renewable Energy**")
    renewable_pct = st.slider(
        "% electricity from renewables",
        min_value=0,
        max_value=100,
        value=50,
        step=5,
        help="Percentage of electricity sourced from solar/wind"
    )

with col_sim3:
    st.markdown("**🌲 Afforestation**")
    added_plantation = st.slider(
        "Additional plantation (hectares)",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=5.0,
        help="Additional land for tree plantation"
    )
    
    added_trees_sim = st.slider(
        "Additional trees planted",
        min_value=0,
        max_value=10000,
        value=2000,
        step=500,
        help="Number of additional trees"
    )

st.markdown("---")

# Run combined simulation
sim_result = combined_simulation(
    diesel_em, electricity_kwh, total_absorption_kg,
    electrification_pct, renewable_pct,
    added_plantation, added_trees_sim
)

# Calculate new totals
new_diesel_em = sim_result['diesel_emissions']
new_electricity_em = sim_result['electricity_emissions']
new_total_em = new_diesel_em + new_electricity_em + excavation_em + transport_em
new_absorption = sim_result['total_absorption']

new_total_em_tonnes = new_total_em / 1000
new_absorption_tonnes = new_absorption / 1000
new_gap_tonnes = (new_total_em - new_absorption) / 1000

# Display simulation results
st.subheader("📊 Simulation Results")

# Single comprehensive comparison chart
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 7))

# Data
categories = ['Emissions\n(Before)', 'Sinks\n(Before)', 'Net Gap\n(After Simulation)']
x = np.arange(len(categories))
width = 0.6

# Values
values = [total_em_tonnes, total_absorption_tonnes, new_gap_tonnes]

# Colors - red for emissions, green for sinks, orange/blue for gap based on positive/negative
colors = ['#E74C3C', '#27AE60', '#F39C12' if new_gap_tonnes > 0 else '#3498DB']

# Create bars
bars = ax.bar(x, values, width, color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar, val in zip(bars, values):
    height = bar.get_height()
    label_y = height if height > 0 else 0
    ax.text(bar.get_x() + bar.get_width()/2., label_y,
            f'{abs(val):.1f} tonnes',
            ha='center', va='bottom' if height > 0 else 'top', 
            fontsize=12, fontweight='bold')

# Add status text for the net gap
if new_gap_tonnes > 0:
    status_text = 'Still Carbon Positive'
    status_color = '#E67E22'
elif new_gap_tonnes < 0:
    status_text = 'Carbon Negative! ✓'
    status_color = '#27AE60'
else:
    status_text = 'Carbon Neutral ✓'
    status_color = '#3498DB'

ax.text(2, max(values) * 0.9, status_text, 
        ha='center', fontsize=11, fontweight='bold', 
        color=status_color, bbox=dict(boxstyle='round,pad=0.5', 
        facecolor='white', edgecolor=status_color, linewidth=2))

ax.set_ylabel('CO₂ (tonnes/year)', fontsize=13, fontweight='bold')
ax.set_title('Simulation Impact Analysis', fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add a horizontal line at y=0 for reference
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)

plt.tight_layout()
st.pyplot(fig)

# Impact summary metrics
col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    reduction = total_em_tonnes - new_total_em_tonnes
    st.metric("Emission Reduction", f"{reduction:.2f} tonnes", 
              f"-{(reduction/total_em_tonnes*100):.1f}%" if total_em_tonnes > 0 else "0%")

with col_m2:
    absorption_increase = new_absorption_tonnes - total_absorption_tonnes
    st.metric("Sink Increase", f"+{absorption_increase:.2f} tonnes",
              f"+{(absorption_increase/total_absorption_tonnes*100):.1f}%" if total_absorption_tonnes > 0 else "N/A")

with col_m3:
    gap_improvement = emission_gap_tonnes - new_gap_tonnes
    st.metric("Gap Improvement", f"{gap_improvement:.2f} tonnes",
              "Improved" if gap_improvement > 0 else "No change",
              delta_color="normal" if gap_improvement > 0 else "off")

st.markdown("---")

# Check if all operational inputs are zero
all_inputs_zero = (diesel_litres == 0 and electricity_kwh == 0 and 
                   coal_extracted == 0 and transport_distance == 0)

if all_inputs_zero:
    st.info("ℹ️ **No Production Data Entered:** Your carbon production is currently 0. Please enter operational data in the sidebar to calculate emissions.")
elif new_gap_tonnes > 0:
    credit_cost = calculate_carbon_credits(new_gap_tonnes)
    st.info(f"💰 **Carbon Credit Estimate:** Offsetting the remaining {new_gap_tonnes:.2f} tonnes would cost approximately **${credit_cost:,.2f} USD** at current market rates.")
else:
    st.success("🎉 **Achievement Unlocked:** With these strategies, your operation would be carbon neutral!")

st.markdown("---")


# Scenario comparison
st.subheader("📉 Before vs After Comparison")

scenario_names = ['Current State', 'After Simulation']
scenario_values = [total_em_tonnes, new_total_em_tonnes]

fig_comparison = scenario_comparison_chart(scenario_names, scenario_values)
st.pyplot(fig_comparison)

# Check if all operational inputs are zero
all_inputs_zero = (diesel_litres == 0 and electricity_kwh == 0 and 
                   coal_extracted == 0 and transport_distance == 0)

if all_inputs_zero:
    st.info("ℹ️ **No Production Data Entered:** Your carbon production is currently 0. Please enter operational data in the sidebar to calculate emissions.")
elif new_gap_tonnes > 0:
    credit_cost = calculate_carbon_credits(new_gap_tonnes)
    st.info(f"💰 **Carbon Credit Estimate:** Offsetting the remaining {new_gap_tonnes:.2f} tonnes would cost approximately **${credit_cost:,.2f} USD** at current market rates.")
else:
    st.success("🎉 **Achievement Unlocked:** With these strategies, your operation would be carbon neutral!")

st.markdown("---")


# ==========================================
# DETAILED BREAKDOWN
# ==========================================

with st.expander("📋 View Detailed Breakdown"):
    st.subheader("Current Emissions by Activity")
    
    breakdown_data = {
        'Activity': ['Diesel Combustion', 'Electricity', 'Excavation', 'Transportation'],
        'Emissions (kg)': [diesel_em, electricity_em, excavation_em, transport_em],
        'Emissions (tonnes)': [
            diesel_em/1000, 
            electricity_em/1000, 
            excavation_em/1000, 
            transport_em/1000
        ],
        'Percentage': [
            (diesel_em/total_em*100) if total_em > 0 else 0,
            (electricity_em/total_em*100) if total_em > 0 else 0,
            (excavation_em/total_em*100) if total_em > 0 else 0,
            (transport_em/total_em*100) if total_em > 0 else 0
        ]
    }
    
    df_breakdown = pd.DataFrame(breakdown_data)
    st.dataframe(df_breakdown.style.format({
        'Emissions (kg)': '{:.2f}',
        'Emissions (tonnes)': '{:.2f}',
        'Percentage': '{:.1f}%'
    }))


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 2rem 0;'>
    <strong>CoalZero</strong> | Built for sustainable mining operations<br>
    Data-driven decision support for carbon neutrality planning
</div>
""", unsafe_allow_html=True)