"""
CoalZero - Visualization Module
Functions to create clear, professional charts using Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np


def emissions_vs_sinks_chart(emissions_tonnes, sinks_tonnes):
    """
    Create a bar chart comparing emissions and carbon sinks
    
    Args:
        emissions_tonnes (float): Total emissions in tonnes
        sinks_tonnes (float): Total absorption in tonnes
    
    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    categories = ['Total Emissions', 'Carbon Sinks']
    values = [emissions_tonnes, sinks_tonnes]
    colors = ['#E74C3C', '#27AE60']
    
    bars = ax.bar(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f} tonnes',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('CO₂ (tonnes/year)', fontsize=12, fontweight='bold')
    ax.set_title('Emissions vs Carbon Sinks', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig


def activity_breakdown_chart(diesel_em, electricity_em, excavation_em, transport_em):
    """
    Create a pie chart showing emission breakdown by activity
    
    Args:
        All emissions in kg
    
    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    labels = ['Diesel', 'Electricity', 'Excavation', 'Transportation']
    values = [diesel_em, electricity_em, excavation_em, transport_em]
    colors = ["#FF6161", "#44A7F2", "#F1C40F", "#925DE8"]
    
    # Filter out zero values
    non_zero = [(l, v, c) for l, v, c in zip(labels, values, colors) if v > 0]
    
    # Check if all values are zero
    if not non_zero or sum(values) == 0:
        # Display a message instead of empty pie chart
        ax.text(0.5, 0.5, 'No emissions data\nEnter operational values to see breakdown', 
                ha='center', va='center', fontsize=14, color='#888',
                transform=ax.transAxes, bbox=dict(boxstyle='round', 
                facecolor='wheat', alpha=0.3))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title('Emission Sources Breakdown', fontsize=14, fontweight='bold', pad=20)
    else:
        labels, values, colors = zip(*non_zero)
        
        wedges, texts, autotexts = ax.pie(values, labels=labels, colors=colors,
                                            autopct='%1.1f%%', startangle=90,
                                            textprops={'fontsize': 11, 'weight': 'bold'})
        
        ax.set_title('Emission Sources Breakdown', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig


def before_after_comparison(before_emissions, after_emissions, strategy_name):
    """
    Create a comparison chart for before/after simulation
    
    Args:
        before_emissions (float): Original emissions in tonnes
        after_emissions (float): Simulated emissions in tonnes
        strategy_name (str): Name of the strategy
    
    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    categories = ['Before', 'After Simulation']
    values = [before_emissions, after_emissions]
    colors = ['#E74C3C', '#27AE60']
    
    bars = ax.bar(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f} tonnes',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    reduction = before_emissions - after_emissions
    reduction_pct = (reduction / before_emissions * 100) if before_emissions > 0 else 0
    
    ax.set_ylabel('CO₂ Emissions (tonnes/year)', fontsize=12, fontweight='bold')
    ax.set_title(f'{strategy_name}\nReduction: {reduction:.2f} tonnes ({reduction_pct:.1f}%)', 
                 fontsize=13, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig


def scenario_comparison_chart(scenario_names, emission_values):
    """
    Compare multiple scenarios side by side
    
    Args:
        scenario_names (list): List of scenario names
        emission_values (list): List of emission values in tonnes
    
    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(scenario_names)))
    bars = ax.bar(scenario_names, emission_values, color=colors, 
                   alpha=0.85, edgecolor='black', linewidth=1.2)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylabel('CO₂ Emissions (tonnes/year)', fontsize=12, fontweight='bold')
    ax.set_title('Scenario Comparison', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=15, ha='right')
    
    plt.tight_layout()
    return fig


def gap_analysis_chart(emissions, sinks, gap):
    """
    Visual representation of emission gap
    
    Args:
        emissions (float): Total emissions in tonnes
        sinks (float): Total sinks in tonnes
        gap (float): Emission gap in tonnes
    
    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    categories = ['Emissions', 'Sinks', 'Gap']
    values = [emissions, sinks, abs(gap)]
    colors = ['#E74C3C', '#27AE60', '#F39C12' if gap > 0 else '#3498DB']
    
    bars = ax.bar(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    status = "Carbon Positive ⚠️" if gap > 0 else "Carbon Neutral ✅"
    ax.set_ylabel('CO₂ (tonnes/year)', fontsize=12, fontweight='bold')
    ax.set_title(f'Gap Analysis — Status: {status}', fontsize=13, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig