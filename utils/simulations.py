"""
CoalZero - Simulation Module
What-if scenario modeling for emission reduction strategies
"""

from utils.emission_factors import (
    ELECTRICITY_EMISSION_FACTOR,
    RENEWABLE_EMISSION_FACTOR,
    CARBON_CREDIT_PRICE,
    KG_TO_TONNES
)


def simulate_electrification(diesel_emissions, electrification_percent):
    """
    Simulate reduction in diesel emissions through electrification
    
    Args:
        diesel_emissions (float): Current diesel emissions in kg
        electrification_percent (float): Percentage of fleet to electrify (0-100)
    
    Returns:
        float: Reduced diesel emissions in kg
    """
    reduction_factor = (100 - electrification_percent) / 100
    return diesel_emissions * reduction_factor


def simulate_renewable_energy(electricity_kwh, renewable_percent):
    """
    Simulate reduction in electricity emissions through renewable adoption
    
    Args:
        electricity_kwh (float): Total electricity consumption in kWh
        renewable_percent (float): Percentage from renewable sources (0-100)
    
    Returns:
        dict: New emissions breakdown
    """
    grid_percent = (100 - renewable_percent) / 100
    renewable_fraction = renewable_percent / 100
    
    grid_emissions = electricity_kwh * grid_percent * ELECTRICITY_EMISSION_FACTOR
    renewable_emissions = electricity_kwh * renewable_fraction * RENEWABLE_EMISSION_FACTOR
    
    total_new_emissions = grid_emissions + renewable_emissions
    
    return {
        'total': total_new_emissions,
        'grid': grid_emissions,
        'renewable': renewable_emissions
    }


def simulate_afforestation(current_absorption, added_area_hectares, added_trees):
    """
    Simulate increased absorption through afforestation
    
    Args:
        current_absorption (float): Current absorption in kg/year
        added_area_hectares (float): Additional plantation area
        added_trees (int): Additional trees planted
    
    Returns:
        float: New total absorption in kg/year
    """
    from utils.sinks import carbon_absorption_from_area, carbon_absorption_from_trees
    
    new_area_absorption = carbon_absorption_from_area(added_area_hectares)
    new_tree_absorption = carbon_absorption_from_trees(added_trees)
    
    return current_absorption + new_area_absorption + new_tree_absorption


def calculate_carbon_credits(emission_gap_tonnes):
    """
    Calculate indicative carbon credit cost for remaining emissions
    
    Args:
        emission_gap_tonnes (float): Remaining emissions in tonnes
    
    Returns:
        float: Estimated cost in USD
    """
    if emission_gap_tonnes <= 0:
        return 0
    return emission_gap_tonnes * CARBON_CREDIT_PRICE


def combined_simulation(diesel_em, electricity_kwh, current_absorption,
                       electrification_pct, renewable_pct, 
                       added_area, added_trees):
    """
    Run combined simulation of all strategies
    
    Returns:
        dict: Comprehensive simulation results
    """
    # Calculate new emissions
    new_diesel_em = simulate_electrification(diesel_em, electrification_pct)
    new_elec_result = simulate_renewable_energy(electricity_kwh, renewable_pct)
    
    # Calculate new absorption
    new_absorption = simulate_afforestation(current_absorption, added_area, added_trees)
    
    return {
        'diesel_emissions': new_diesel_em,
        'electricity_emissions': new_elec_result['total'],
        'total_absorption': new_absorption
    }