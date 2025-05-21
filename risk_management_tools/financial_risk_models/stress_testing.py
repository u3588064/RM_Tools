import numpy as np
import pandas as pd

def apply_scenario_to_portfolio(portfolio, scenario_shocks, correlation_matrix=None):
    """
    Apply a stress test scenario to a portfolio and calculate the impact.
    
    Args:
        portfolio (dict): Dictionary with asset names as keys and their values/exposures as values.
        scenario_shocks (dict): Dictionary with asset names as keys and their expected percentage changes as values.
        correlation_matrix (pd.DataFrame, optional): Correlation matrix between assets for more accurate stress testing.
        
    Returns:
        dict: Dictionary containing the original portfolio, stressed portfolio, and impact details.
    """
    if not portfolio or not scenario_shocks:
        print("Error: Portfolio or scenario shocks cannot be empty.")
        return None
    
    # Initialize results
    original_total = sum(portfolio.values())
    stressed_portfolio = {}
    asset_impacts = {}
    
    # Apply shocks to each asset
    for asset, value in portfolio.items():
        shock = scenario_shocks.get(asset, 0)  # Default to 0 if asset not in scenario
        stressed_value = value * (1 + shock)
        stressed_portfolio[asset] = stressed_value
        asset_impacts[asset] = {
            "original_value": value,
            "shock_percentage": shock * 100,
            "stressed_value": stressed_value,
            "impact_amount": stressed_value - value,
            "impact_percentage": ((stressed_value - value) / value) * 100 if value != 0 else 0
        }
    
    # Calculate total impact
    stressed_total = sum(stressed_portfolio.values())
    total_impact = stressed_total - original_total
    total_impact_percentage = (total_impact / original_total) * 100 if original_total != 0 else 0
    
    # Print results
    print("\n--- Stress Test Results ---")
    print(f"Original Portfolio Value: ${original_total:,.2f}")
    print(f"Stressed Portfolio Value: ${stressed_total:,.2f}")
    print(f"Total Impact: ${total_impact:,.2f} ({total_impact_percentage:.2f}%)")
    print("\nImpact by Asset:")
    for asset, impact in asset_impacts.items():
        print(f"  {asset}: ${impact['impact_amount']:,.2f} ({impact['impact_percentage']:.2f}%)")
    
    return {
        "original_portfolio": portfolio,
        "original_total": original_total,
        "stressed_portfolio": stressed_portfolio,
        "stressed_total": stressed_total,
        "total_impact": total_impact,
        "total_impact_percentage": total_impact_percentage,
        "asset_impacts": asset_impacts
    }

def define_historical_scenario(scenario_name, description, asset_shocks):
    """
    Define a historical stress test scenario.
    
    Args:
        scenario_name (str): Name of the historical scenario.
        description (str): Description of the scenario.
        asset_shocks (dict): Dictionary with asset classes as keys and their expected percentage changes as values.
        
    Returns:
        dict: A structured scenario definition.
    """
    scenario = {
        "name": scenario_name,
        "description": description,
        "asset_shocks": asset_shocks,
        "type": "historical"
    }
    
    print(f"Defined historical scenario: {scenario_name}")
    print(f"Description: {description}")
    print("Asset Shocks:")
    for asset, shock in asset_shocks.items():
        print(f"  {asset}: {shock*100:.2f}%")
    
    return scenario

def define_hypothetical_scenario(scenario_name, description, asset_shocks, probability=None):
    """
    Define a hypothetical stress test scenario.
    
    Args:
        scenario_name (str): Name of the hypothetical scenario.
        description (str): Description of the scenario.
        asset_shocks (dict): Dictionary with asset classes as keys and their expected percentage changes as values.
        probability (float, optional): Estimated probability of the scenario occurring.
        
    Returns:
        dict: A structured scenario definition.
    """
    scenario = {
        "name": scenario_name,
        "description": description,
        "asset_shocks": asset_shocks,
        "type": "hypothetical",
        "probability": probability
    }
    
    print(f"Defined hypothetical scenario: {scenario_name}")
    print(f"Description: {description}")
    if probability is not None:
        print(f"Estimated probability: {probability*100:.2f}%")
    print("Asset Shocks:")
    for asset, shock in asset_shocks.items():
        print(f"  {asset}: {shock*100:.2f}%")
    
    return scenario 