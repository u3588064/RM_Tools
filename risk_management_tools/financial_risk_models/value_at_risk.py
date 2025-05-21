import numpy as np
from scipy import stats

def calculate_historical_var(returns, confidence_level=0.95, investment_value=1000000):
    """
    Calculate Value at Risk (VaR) using the historical simulation method.
    
    Args:
        returns (list or numpy.array): Historical returns data (e.g., daily returns).
        confidence_level (float): Confidence level for VaR calculation (e.g., 0.95 for 95%).
        investment_value (float): Current value of the investment or portfolio.
        
    Returns:
        float: The Value at Risk amount at the specified confidence level.
    """
    if not isinstance(returns, np.ndarray):
        returns = np.array(returns)
    
    # Sort returns from worst to best
    sorted_returns = np.sort(returns)
    
    # Find the index at the confidence level
    index = int(np.ceil(len(sorted_returns) * (1 - confidence_level)) - 1)
    
    # Ensure the index is valid
    if index < 0:
        index = 0
    
    # Get the return at the confidence level
    var_return = sorted_returns[index]
    
    # Calculate the monetary VaR
    var_amount = investment_value * -var_return
    
    print(f"Historical VaR at {confidence_level*100}% confidence: ${var_amount:.2f}")
    print(f"This means there is a {(1-confidence_level)*100}% chance of losing more than ${var_amount:.2f} in a single period.")
    
    return var_amount

def calculate_parametric_var(mean_return, std_dev, confidence_level=0.95, investment_value=1000000, time_horizon=1):
    """
    Calculate Value at Risk (VaR) using the parametric method (assuming normal distribution).
    
    Args:
        mean_return (float): Mean of returns (e.g., daily mean return).
        std_dev (float): Standard deviation of returns.
        confidence_level (float): Confidence level for VaR calculation (e.g., 0.95 for 95%).
        investment_value (float): Current value of the investment or portfolio.
        time_horizon (int): Time horizon in days for scaling VaR.
        
    Returns:
        float: The Value at Risk amount at the specified confidence level.
    """
    # Calculate Z-score for the given confidence level
    z_score = stats.norm.ppf(1 - confidence_level)
    
    # Calculate VaR
    var_return = -(mean_return * time_horizon + z_score * std_dev * np.sqrt(time_horizon))
    var_amount = investment_value * var_return
    
    print(f"Parametric VaR at {confidence_level*100}% confidence over {time_horizon} day(s): ${var_amount:.2f}")
    print(f"This means there is a {(1-confidence_level)*100}% chance of losing more than ${var_amount:.2f} in {time_horizon} day(s).")
    
    return var_amount

def calculate_conditional_var(returns, confidence_level=0.95, investment_value=1000000):
    """
    Calculate Conditional Value at Risk (CVaR), also known as Expected Shortfall.
    This represents the expected loss given that the loss exceeds VaR.
    
    Args:
        returns (list or numpy.array): Historical returns data.
        confidence_level (float): Confidence level for CVaR calculation.
        investment_value (float): Current value of the investment or portfolio.
        
    Returns:
        float: The Conditional Value at Risk amount at the specified confidence level.
    """
    if not isinstance(returns, np.ndarray):
        returns = np.array(returns)
    
    # Sort returns from worst to best
    sorted_returns = np.sort(returns)
    
    # Find the index at the confidence level
    index = int(np.ceil(len(sorted_returns) * (1 - confidence_level)) - 1)
    
    # Ensure the index is valid
    if index < 0:
        index = 0
    
    # Calculate CVaR as the average of losses beyond VaR
    cvar_returns = sorted_returns[:index+1]
    cvar_return = np.mean(cvar_returns)
    
    # Calculate the monetary CVaR
    cvar_amount = investment_value * -cvar_return
    
    print(f"Conditional VaR at {confidence_level*100}% confidence: ${cvar_amount:.2f}")
    print(f"This is the expected loss when losses exceed the VaR threshold.")
    
    return cvar_amount 