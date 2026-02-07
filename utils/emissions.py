"""
CoalZero - Emission Calculation Module
Functions to calculate carbon emissions from various mining activities
"""

from utils.emission_factors import (
    DIESEL_EMISSION_FACTOR,
    ELECTRICITY_EMISSION_FACTOR,
    COAL_EXCAVATION_FACTOR,
    TRANSPORTATION_FACTOR,
    KG_TO_TONNES
)


def diesel_emissions(litres):
    """
    Calculate CO2 emissions from diesel consumption
    
    Args:
        litres (float): Diesel consumed in litres
    
    Returns:
        float: CO2 emissions in kg
    """
    return litres * DIESEL_EMISSION_FACTOR


def electricity_emissions(kwh):
    """
    Calculate CO2 emissions from electricity consumption
    
    Args:
        kwh (float): Electricity consumed in kWh
    
    Returns:
        float: CO2 emissions in kg
    """
    return kwh * ELECTRICITY_EMISSION_FACTOR


def excavation_emissions(coal_tonnes):
    """
    Calculate CO2 emissions from coal excavation
    
    Args:
        coal_tonnes (float): Tonnes of coal excavated
    
    Returns:
        float: CO2 emissions in kg
    """
    return coal_tonnes * COAL_EXCAVATION_FACTOR


def transportation_emissions(coal_tonnes, distance_km):
    """
    Calculate CO2 emissions from coal transportation
    
    Args:
        coal_tonnes (float): Tonnes of coal transported
        distance_km (float): Distance transported in km
    
    Returns:
        float: CO2 emissions in kg
    """
    return coal_tonnes * distance_km * TRANSPORTATION_FACTOR


def total_emissions(diesel_em, electricity_em, excavation_em, transport_em):
    """
    Calculate total emissions from all activities
    
    Args:
        diesel_em (float): Diesel emissions in kg
        electricity_em (float): Electricity emissions in kg
        excavation_em (float): Excavation emissions in kg
        transport_em (float): Transportation emissions in kg
    
    Returns:
        float: Total emissions in kg
    """
    return diesel_em + electricity_em + excavation_em + transport_em


def per_capita_emissions(total_em, workers):
    """
    Calculate per-capita emissions
    
    Args:
        total_em (float): Total emissions in kg
        workers (int): Number of workers
    
    Returns:
        float: Per-capita emissions in kg/person
    """
    if workers == 0:
        return 0
    return total_em / workers


def emissions_in_tonnes(emissions_kg):
    """
    Convert emissions from kg to tonnes
    
    Args:
        emissions_kg (float): Emissions in kg
    
    Returns:
        float: Emissions in tonnes
    """
    return emissions_kg / KG_TO_TONNES