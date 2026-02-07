"""
CoalZero - Emission Factors and Constants
This file contains all emission factors, absorption rates, and assumptions
used throughout the application.
"""

# ==========================================
# EMISSION FACTORS
# ==========================================

# Diesel combustion (kg CO2 per litre)
DIESEL_EMISSION_FACTOR = 2.68  # kg CO2/litre

# Electricity from grid (kg CO2 per kWh)
# Assumes coal-dominated grid mix
ELECTRICITY_EMISSION_FACTOR = 0.82  # kg CO2/kWh

# Coal excavation (kg CO2 per tonne of coal extracted)
# Includes machinery, blasting, etc.
COAL_EXCAVATION_FACTOR = 0.15  # kg CO2/tonne

# Transportation - Heavy trucks (kg CO2 per km per tonne)
TRANSPORTATION_FACTOR = 0.062  # kg CO2/tonne-km

# ==========================================
# CARBON ABSORPTION CONSTANTS
# ==========================================

# Carbon absorption per hectare per year (mature forest)
ABSORPTION_PER_HECTARE = 10000  # kg CO2/hectare/year

# Average carbon absorbed per tree per year
ABSORPTION_PER_TREE = 22  # kg CO2/tree/year

# ==========================================
# RENEWABLE ENERGY FACTORS
# ==========================================

# Emission factor for renewable energy (nearly zero)
RENEWABLE_EMISSION_FACTOR = 0.02  # kg CO2/kWh (minimal lifecycle emissions)

# ==========================================
# CARBON CREDIT PRICING
# ==========================================

# Indicative carbon credit price (USD per tonne CO2)
CARBON_CREDIT_PRICE = 15  # USD/tonne CO2

# ==========================================
# CONVERSION FACTORS
# ==========================================

# kg to tonnes
KG_TO_TONNES = 1000

# Hectares to acres
HECTARE_TO_ACRE = 2.47