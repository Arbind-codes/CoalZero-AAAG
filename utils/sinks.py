"""
CoalZero - Carbon Sink Estimation Module
Functions to estimate carbon absorption from plantations and green cover
"""

from utils.emission_factors import (
    ABSORPTION_PER_HECTARE,
    ABSORPTION_PER_TREE,
    KG_TO_TONNES
)


def carbon_absorption_from_area(area_hectares):
    """
    Calculate carbon absorption from plantation area
    
    Args:
        area_hectares (float): Plantation area in hectares
    
    Returns:
        float: Carbon absorbed in kg/year
    """
    return area_hectares * ABSORPTION_PER_HECTARE


def carbon_absorption_from_trees(num_trees):
    """
    Calculate carbon absorption from number of trees
    
    Args:
        num_trees (int): Number of trees
    
    Returns:
        float: Carbon absorbed in kg/year
    """
    return num_trees * ABSORPTION_PER_TREE


def total_absorption(area_hectares, num_trees):
    """
    Calculate total carbon absorption from all sources
    
    Args:
        area_hectares (float): Plantation area in hectares
        num_trees (int): Number of additional trees
    
    Returns:
        float: Total carbon absorbed in kg/year
    """
    area_absorption = carbon_absorption_from_area(area_hectares)
    tree_absorption = carbon_absorption_from_trees(num_trees)
    return area_absorption + tree_absorption


def absorption_in_tonnes(absorption_kg):
    """
    Convert absorption from kg to tonnes
    
    Args:
        absorption_kg (float): Absorption in kg
    
    Returns:
        float: Absorption in tonnes
    """
    return absorption_kg / KG_TO_TONNES


def land_required_for_neutrality(emission_gap_kg):
    """
    Calculate land area required to offset remaining emissions


    Args:
        emission_gap_kg (float): Remaining emissions in kg
    
    Returns:
        float: Required plantation area in hectares
    """
    if emission_gap_kg <= 0:
        return 0
    return emission_gap_kg / ABSORPTION_PER_HECTARE